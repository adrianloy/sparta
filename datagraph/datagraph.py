from app.auxiliary import *
from parsers.HydraParser import *
from parsers.W3afParser import *
from parsers.NiktoParser import *
from parsers.ZapParser import *


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
                self.host_dict[host.id] = host_node
                self.view.ui.addNodeTo(self.root.node_id, host_node_id, host.ip + " (" + host.hostname + ")", "hosts")

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
        # insert process when not already inserted
        processes = self.view.controller.getProcessesWithPortIdFromDB()
        for process in processes:
            if process.id not in self.tool_dict:
                port_id = process.port_id
                if port_id not in self.port_dict:
                    print "error importing process from db (port id " + str(port_id) + " not in port_dict)"
                    continue
                port_node = self.port_dict[port_id]
                process_node = ToolNode(self, process.id, process.name, process.output, process.outputfile)
                process_node_id = port_node.add_child(process_node)
                self.tool_dict[process.id] = process_node
                self.view.ui.addNodeTo(port_node.node_id, process_node_id, process.name, "processes")
                # TODO: find better solution
                if 'Nikto' in process.output:
                    NiktoParser.create_issue_nodes(process_node)
                if 'ZAP' in process.output:
                    ZapParser.create_issue_nodes(process_node)
                if 'Hydra' in process.output:
                    HydraParser.create_issue_nodes(process_node)
                if 'w3af' in process.output:
                    W3afParser.create_issue_nodes(process_node)

    def save_as_xml(self):
        scan = bind.scan()
        scan.dateTime = datetime.datetime.now()
        scan.host = []
        for child in self.root.children:
            scan.host.append(child.generate_dom())

        output = scan.toDOM(None).toprettyxml(indent="  ")
        with open('output.xml', 'w') as f:
            f.write(output)
