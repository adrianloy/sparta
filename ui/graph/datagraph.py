from node import *
from app.auxiliary import *


class DataGraph(Node):

    def __init__(self, view):
        self.root_ = Node(self)
        self.counter_ = 1
        self.nodes_ = {0: self.root_}
        self.view_ = view

    def get_new_id(self):
        new_id = self.counter_
        self.counter_ += 1
        return new_id

    def get_node(self, node_id):
        return self.nodes_[node_id]

    def update_graph_from_db(self):
        hosts = self.view_.controller.getHostsFromDB(Filters())
        for host in hosts:
            # insert host when not already inserted
            host_node = 0
            if host.id not in self.root_.children_:
                host_node = HostNode(self, host.id, host.ip)
                host_node_id = self.root_.add_child(host_node)
                self.view_.ui.addNodeTo(self.root_.node_id_, host_node_id, host.ip, "hosts")
            else:
                host_node = self.root_.children_[host.id]

            # insert port when not already inserted
            ports = self.view_.controller.getPortsForHostId(host.id)
            for port in ports:
                if port.port_id not in host_node.children_:
                    port_node = PortNode(self, port.port_id, port.port_id, port.name)
                    port_node_id = host_node.add_child(port_node)
                    self.view_.ui.addNodeTo(host_node.node_id_, port_node_id, port.port_id + "/" + port.protocol + " (" + port.name + ")", "ports")

            # insert process when not already inserted
            processes = self.view_.controller.getProcessesForHostId(host_node.node_id_)
            for process in processes:
                if process.port == "":
                    continue
                if process.port not in host_node.children_:
                    print "error: port node not available"
                    continue
                port_node = host_node.children_[process.port]
                if process.id not in port_node.children_:
                    new_process_node = ProcessNode(self, process.id, process.name, process.output)
                    new_node_id = port_node.add_child(new_process_node)
                    self.view_.ui.addNodeTo(port_node.node_id_, new_node_id, process.name, "processes")
