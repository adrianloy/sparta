from node import *
from app.auxiliary import *
import xml_schema.binding as bind
import app.logic as logic
from parsers.ToolParsers import *


class DataGraph(object):

    def __init__(self, view):
        self.root = Node(self)
        self.counter = 1
        self.nodes = {0: self.root}
        self.view = view
        self.host_dict = {}
        self.port_dict = {}
        self.vul_dict = {}
        self.process_dict = {}

    def get_new_id(self):
        new_id = self.counter
        self.counter += 1
        return new_id

    def get_node(self, node_id):
        return self.nodes[node_id]

    def getHostNodeByIP(self, ip): #normally host list is short so its fine
        for node in self.host_dict.values():
            if node.host_ip == ip:
                return node

    def clear(self):
        self.root = Node(self)
        self.counter = 1
        self.nodes = {0: self.root}
        self.host_dict = {}
        self.port_dict = {}
        self.process_dict = {}

    def build_graph_from_db(self):
        # insert host when not already inserted
        hosts = self.view.controller.getHostsFromDB(Filters())
        for host in hosts:
            if host.id not in self.host_dict:
                host_node = HostNode(self, host.id, host.ip)
                host_node_id = self.root.add_child(host_node)
                self.host_dict[host.id] = host_node
                self.view.ui.addNodeTo(self.root.node_id, host_node_id, host.ip, "hosts")

        # insert port when not already inserted
        ports = self.view.controller.getPortsFromDB()
        for port in ports:
            if port.id not in self.port_dict:
                host_id = port.host_id
                if host_id not in self.host_dict:
                    print "error importing ports from db (host id " + str(host_id) + " not in host_dict)"
                    continue
                host_node = self.host_dict[host_id]
                port_node = PortNode(self, port.id, port.number, port.name)
                port_node_id = host_node.add_child(port_node)
                self.port_dict[port.id] = port_node
                self.view.ui.addNodeTo(host_node.node_id, port_node_id, port.number + "/" + port.protocol + " (" + port.name + ")", "ports")

        # insert process when not already inserted
        processes = self.view.controller.getProcessesWithPortIdFromDB()
        for process in processes:
            if process.id not in self.process_dict:
                port_id = process.port_id
                if port_id not in self.port_dict:
                    print "error importing process from db (port id " + str(port_id) + " not in port_dict)"
                    continue
                port_node = self.port_dict[port_id]
                process_node = ProcessNode(self, process.id, process.name, process.output)
                process_node_id = port_node.add_child(process_node)
                self.process_dict[process.id] = process_node
                self.view.ui.addNodeTo(port_node.node_id, process_node_id, process.name, "processes")

        #parse the w3af xml output file to generate vulnodes
        #the file is located in the outputfolder, that is copied when saving the project
        #path is not in db but is built from the location to the saved file, so we need the logic obj
        #print(self.controller.logic.outputfolder + '/w3af')
        w3dir = self.view.controller.logic.outputfolder + '/w3af/'
        if os.path.isdir(w3dir):
            for filename in os.listdir(w3dir):
                #if filename.endswith(".asm") or filename.endswith(".py"):
                myparser = W3afParser(self, w3dir+filename)
                ip = myparser.getHost()
                port = myparser.getPort()
                grandfather = self.getHostNodeByIP(ip)
                parent = grandfather.portNodeDict[port]
                for vulNode in myparser.getVulNodes():
                    vulNodeID = parent.add_child(vulNode)
                    self.view.ui.addNodeTo(parent.node_id, vulNodeID, vulNode.name, "vulnerabilities")
                    self.vul_dict[vulNodeID] = vulNode


    def save_as_xml(self):
        scan = bind.scan()
        scan.dateTime = datetime.datetime.now()
        scan.host = []
        for child in self.root.children:
            scan.host.append(child.generate_dom())

        xml = scan.toDOM(None).toprettyxml(indent="  ")
        with open('output.xml', 'w') as f:
            f.write(xml)
