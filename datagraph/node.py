import xml_schema.binding as bind


class Node(object):

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

    def add_childlist(self, childlist):
        childIDs = []
        for child in childlist:
            childIDs.append(self.add_child(child))
        return childIDs

    def generate_dom(self):
        return


class HostNode(Node):

    def __init__(self, data_graph, host_id, host_ip):
        Node.__init__(self, data_graph)
        self.host_id_ = host_id
        self.host_ip_ = host_ip

    def generate_dom(self):
        host = bind.host()
        host.ip = self.host_ip_
        host.port = []
        for child in self.children_:
            if type(child) is not VulNode: #TODO adapt vulnode class
                host.port.append(child.generate_dom())
        return host


class PortNode(Node):

    def __init__(self, data_graph, port_id, port, standard_service_name):
        Node.__init__(self, data_graph)
        self.port_id_ = port_id
        self.port_ = port
        self.standard_service_name_ = standard_service_name

    def generate_dom(self):
        port = bind.port()
        port.port = self.port_
        port.standardService = self.standard_service_name_
        port.issue = []
        for child in self.children_:
            port.issue.append(child.generate_dom())
        return port


class ProcessNode(Node):

    def __init__(self, data_graph, process_id, process_name, process_output):
        Node.__init__(self, data_graph)
        self.process_id_ = process_id
        self.process_name_ = process_name
        self.process_output_ = process_output

    def generate_dom(self):
        issue = bind.issue()
        issue.tool = self.process_name_
        issue.text = self.process_output_
        return issue


class VulNode(Node):

    def __init__(self, data_graph, severity, url,name, descr, longdescr, fixstr):
        Node.__init__(self, data_graph)
        self.severity = severity
        self.url = url
        self.name = name
        self.descr = descr
        self.longdescr = longdescr
        self.fixstr = fixstr

    #def generate_dom(self):
    #    issue = bind.issue()
    #    issue.tool = self.name
    #    issue.text = self.descr
    #    return issue
