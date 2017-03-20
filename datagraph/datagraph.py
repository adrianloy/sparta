from app.auxiliary import *
from parsers.HydraParser import *
from parsers.W3afParser import *
from parsers.NiktoParser import *
from parsers.ZapParser import *
from parsers.NessusParser import *
from parsers.OS import *


class DataGraph(object):

    def __init__(self, view):
        self.root = Node(self)
        self.counter = 1
        self.nodes = {0: self.root}
        self.view = view
        self.host_dict = {}
        self.port_dict = {}
        self.issue_dict = {}
        self.tool_dict = {}

    def get_new_id(self):
        new_id = self.counter
        self.counter += 1
        return new_id

    def get_node(self, node_id):
        return self.nodes[node_id]

    def clear(self):
        self.root = Node(self)
        self.counter = 1
        self.nodes = {0: self.root}
        self.host_dict = {}
        self.port_dict = {}
        self.tool_dict = {}
        self.issue_dict = {}

    def build_graph_from_db(self):
        self.create_host_nodes_from_db()
        self.create_port_nodes_from_db()
        self.create_tool_nodes_from_db()

    def create_host_nodes_from_db(self):
        # insert host when not already inserted
        hosts = self.view.controller.getHostsFromDB(Filters())
        for host in hosts:
            if host.id not in self.host_dict:
                host_node = HostNode(self, host.id, host.ip, host.hostname)
                host_node_id = self.root.add_child(host_node)

                nmap_host = self.view.controller.getHostInformation(host.ip)
                os_match = nmap_host.os_match
                if os_match != "" and os_match is not None:
                    os_accuracy = nmap_host.os_accuracy
                    os_vendor = nmap_host.vendor
                    host_node.os += "Nmap:\nName: " + os_match + "\nVendor: " + os_vendor + \
                                    "\nAccuracy: " + os_accuracy + "\n"
                   # print(str(host_node.os))

                self.host_dict[host.id] = host_node
                self.view.ui.addNodeTo(self.root.node_id, host_node_id, host.ip + " (" + host.hostname + ")", "hosts")



    def getHostNodeByIP(self, ipstr):
        for host in self.host_dict.values():
            if host.ip == ipstr:
                return host

    def create_port_nodes_from_db(self):
        # insert port when not already inserted
        ports = self.view.controller.getPortsFromDB()
        for port in ports:
            if port.id not in self.port_dict:
                host_id = port.host_id
                if host_id not in self.host_dict:
                    print "error importing ports from db (host id " + str(host_id) + " not in host_dict)"
                    continue
                host_node = self.host_dict[host_id]
                port_node = PortNode(self, port.id, port.number, port.name, port.protocol)
                port_node_id = host_node.add_child(port_node)
                self.port_dict[port.id] = port_node
                self.view.ui.addNodeTo(host_node.node_id, port_node_id,
                                       port.number + "/" + port.protocol + " (" + port.name + ")", "ports")

    def create_tool_nodes_from_db(self):
        # insert process to port nodes when not already inserted
        processes = self.view.controller.getProcessesWithPortIdFromDB()
        for tool in processes:
            if tool.id not in self.tool_dict:
                port_id = tool.port_id
                if port_id not in self.port_dict:
                    print "error importing process from db (port id " + str(port_id) + " not in port_dict)"
                    continue
                port_node = self.port_dict[port_id]
                tool_node = ToolNode(self, tool.id, tool.name, tool.output, tool.outputfile)
                tool_node_id = port_node.add_child(tool_node)
                self.tool_dict[tool.id] = tool_node
                self.view.ui.addNodeTo(port_node.node_id, tool_node_id, tool.name, "tools")
                # TODO: find better solution
                if 'Nikto' in tool.output:
                    NiktoParser.create_issue_nodes(tool_node)
                if 'ZAP' in tool.output:
                    ZapParser.create_issue_nodes(tool_node)
                if 'Hydra' in tool.output:
                    HydraParser.create_issue_nodes(tool_node)
                if 'w3af' in tool.output:
                    W3afParser.create_issue_nodes(tool_node)
                if 'nessus' in tool_node.outputfile:
                    NessusParser.create_issue_nodes(tool_node)
        # insert process to host nodes (like nessus) when not already inserted
        processes = self.view.controller.getSpecificProcessWithOutputFromDB('nessus')
        for tool in processes:
            if tool.id not in self.tool_dict:
                host_node = self.getHostNodeByIP(tool.hostip)
                if host_node is None:
                    print "error importing process from db: Cant find host node with ip" + str(tool.hostip)
                    continue
                tool_node = ToolNode(self, tool.id, tool.name, tool.output, tool.outputfile)
                tool_node_id = host_node.add_child(tool_node)
                self.tool_dict[tool.id] = tool_node
                self.view.ui.addNodeTo(host_node.node_id, tool_node_id, tool.name, "tools")
                # TODO: find better solution
                if 'nessus' in tool_node.outputfile:
                    NessusParser.create_issue_nodes(tool_node)
                    nesOS = NessusParser.getOSDetection(tool_node)
                    if nesOS:
                        host_node.os = host_node.os + "Nessus: \n"+self.OS_obj_stringrepr(nesOS)


    def save_as_xml(self):
        scan = bind.scan()
        scan.dateTime = datetime.datetime.now()  # TODO: use correct time
        scan.host = []
        for child in self.root.children:
            scan.host.append(child.generate_xml_binding_instance())

        output = scan.toDOM(None).toprettyxml(indent="  ")
        with open('scan_aggregation.xml', 'w') as f:
            f.write(output)

    'Returns a string representing of an OS obj'
    @staticmethod
    def OS_obj_stringrepr(osobj):
        s = ""
        if osobj.name != '' and osobj.name is not None:
            s += "Name: " + osobj.name + "\n"
        if osobj.family != '' and osobj.family is not None:
            s += "Family: " + osobj.family + "\n"
        if osobj.generation != '' and osobj.generation is not None:
            s += "Generation: " + osobj.generation + "\n"
        if osobj.os_type != '' and osobj.os_type is not None:
            s += "Os_type: " + osobj.os_type + "\n"
        if osobj.vendor != '' and osobj.vendor is not None:
            s += "Vendor: " + osobj.vendor + "\n"
        if osobj.accuracy != '' and osobj.accuracy is not None:
            s += "Accuracy: " + osobj.accuracy + ""
        return s