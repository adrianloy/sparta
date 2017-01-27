import xml_schema.binding as bind


class Node(object):

    def __init__(self, data_graph):
        self.node_id = 0
        self.parent_node_id = 0
        self.children = []
        self.data_graph = data_graph

    def add_child(self, child):
        new_id = self.data_graph.get_new_id()
        child.node_id = new_id
        child.parent_node_id = self.node_id
        self.children.append(child)
        self.data_graph.nodes[child.node_id] = child
        return child.node_id

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
        self.host_id = host_id
        self.host_ip = host_ip

    def generate_dom(self):
        host = bind.host()
        host.ip = self.host_ip
        host.port = []
        for child in self.children:
            if type(child) is not VulNode: #TODO adapt vulnode class
                host.port.append(child.generate_dom())
        return host


class PortNode(Node):

    def __init__(self, data_graph, port_id, port, standard_service_name):
        Node.__init__(self, data_graph)
        self.port_id = port_id
        self.port = port
        self.standard_service_name = standard_service_name

    def generate_dom(self):
        port = bind.port()
        port.port = self.port
        port.standardService = self.standard_service_name
        port.issue = []
        for child in self.children:
            port.issue.append(child.generate_dom())
        return port


class ProcessNode(Node):

    def __init__(self, data_graph, process_id, process_name, process_output):
        Node.__init__(self, data_graph)
        self.process_id = process_id
        self.process_name = process_name
        self.process_output = process_output

    def generate_dom(self):
        issue = bind.issue()
        issue.tool = self.process_name
        issue.text = self.process_output
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
