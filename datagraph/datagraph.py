from node import *
from app.auxiliary import *
import xml_schema.binding as bind


class DataGraph(object):

    def __init__(self, view):
        self.root_ = Node(self)
        self.counter_ = 1
        self.nodes_ = {0: self.root_}
        self.view_ = view
        self.host_dict_ = {}
        self.port_dict_ = {}
        self.process_dict_ = {}

    def get_new_id(self):
        new_id = self.counter_
        self.counter_ += 1
        return new_id

    def get_node(self, node_id):
        return self.nodes_[node_id]

    def update_graph_from_db(self):
        # insert host when not already inserted
        hosts = self.view_.controller.getHostsFromDB(Filters())
        for host in hosts:
            if host.id not in self.host_dict_:
                host_node = HostNode(self, host.id, host.ip)
                host_node_id = self.root_.add_child(host_node)
                self.host_dict_[host.id] = host_node
                self.view_.ui.addNodeTo(self.root_.node_id_, host_node_id, host.ip, "hosts")

        # insert port when not already inserted
        ports = self.view_.controller.getPortsFromDB()
        for port in ports:
            if port.id not in self.port_dict_:  # port.id is the port id, port.port_id is the port
                host_id = port.host_id
                if host_id not in self.host_dict_:
                    print "error"
                    continue
                host_node = self.host_dict_[host_id]
                port_node = PortNode(self, port.id, port.port_id, port.name)
                port_node_id = host_node.add_child(port_node)
                self.port_dict_[port.id] = port_node
                self.view_.ui.addNodeTo(host_node.node_id_, port_node_id, port.port_id + "/" + port.protocol + " (" + port.name + ")", "ports")

        # insert process when not already inserted
        processes = self.view_.controller.getProcessesWithPortIdFromDB()
        for process in processes:
            if process.id not in self.process_dict_:
                port_id = process.port_id
                if port_id not in self.port_dict_:
                    print "error"
                    continue
                port_node = self.port_dict_[port_id]
                process_node = ProcessNode(self, process.id, process.name, process.output)
                process_node_id = port_node.add_child(process_node)
                self.process_dict_[process.id] = process_node
                self.view_.ui.addNodeTo(port_node.node_id_, process_node_id, process.name, "processes")

    def save_as_xml(self):
        scan = bind.scan()
        scan.dateTime = datetime.datetime.now()
        scan.host = []
        for child in self.root_.children_:
            scan.host.append(child.generate_dom())

        xml = scan.toDOM(None).toprettyxml(indent="  ")
        with open('output.xml', 'w') as f:
            f.write(xml)
