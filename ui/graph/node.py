class Node:
    def __init__(self, data_graph):
        self.node_id_ = 0
        self.parent_node_id_ = 0
        self.children_ = []
        self.data_graph_ = data_graph

    def add_child(self, child):
        new_id = self.data_graph_.get_new_id()
        child.node_id_ = new_id
        child.parent_node_id_ = self.node_id_
        self.children_.append(child)
        self.data_graph_.nodes_[child.node_id_] = child
        return child.node_id_


class HostNode(Node):
    def __init__(self, data_graph, host_id, host_ip):
        Node.__init__(self, data_graph)
        self.host_id_ = host_id
        self.host_ip_ = host_ip


class PortNode(Node):
    def __init__(self, data_graph, port_id, port, standard_service_name):
        Node.__init__(self, data_graph)
        self.port_id_ = port_id
        self.port_ = port
        self.standard_service_name_ = standard_service_name


class ProcessNode(Node):
    def __init__(self, data_graph, process_id, process_name, process_output):
        Node.__init__(self, data_graph)
        self.process_id_ = process_id
        self.process_name_ = process_name
        self.process_output_ = process_output

