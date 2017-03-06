import xml_bindings.aggregation as bind
import os.path
import glob


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

    def add_child_list(self, child_list):
        child_ids = []
        for child in child_list:
            child_ids.append(self.add_child(child))
        return child_ids

    def generate_dom(self):
        return

    def __str__(self):
        result = "Node (id = " + str(self.node_id) + ")"
        return result


class HostNode(Node):

    def __init__(self, data_graph, host_id, host_ip, host_name):
        Node.__init__(self, data_graph)
        self.host_id = host_id
        self.ip = host_ip
        self.name = host_name
        self.portNodeDict = {}

    def add_child(self, child):
        if type(child) is PortNode:
            self.portNodeDict[child.number] = child
        return Node.add_child(self, child)

    def generate_dom(self):
        host = bind.host()
        host.ip = self.ip
        host.hostname = self.name
        host.port = []
        for child in self.children:
            host.port.append(child.generate_dom())
        return host

    def __str__(self):
        result = "HostNode (id = " + str(self.node_id) + ")\n\nIP: " + self.ip + "\nHostname: " + self.name
        return result


class PortNode(Node):

    def __init__(self, data_graph, port_id, port_number, service_name, port_protocol):
        Node.__init__(self, data_graph)
        self.port_id = port_id
        self.number = port_number
        self.protocol = port_protocol
        self.service_name = service_name

    def generate_dom(self):
        port = bind.port()
        port.number = self.number
        port.standardService = self.service_name
        port.tool = []
        port.protocol = self.protocol
        for child in self.children:
            port.tool.append(child.generate_dom())

        return port

    def __str__(self):
        result = "PortNode (id = " + str(self.node_id) + ")\n\nNumber: " + self.number + "\nProtocol: " + \
                 self.protocol + "\nStandard Service: " + self.service_name
        return result


class ToolNode(Node):

    def __init__(self, data_graph, process_id, process_name, process_output, process_output_file):
        Node.__init__(self, data_graph)
        self.process_id = process_id  # in data base it is called process
        self.name = process_name
        self.terminal_output = process_output
        self.outputfile = process_output_file
        self.file_output = ''
        file_candidates = glob.glob(self.outputfile + '*')
        if len(file_candidates) == 1:
            self.file_output = open(file_candidates[0], 'r').read()
        else:
            print 'info: ' + str(len(file_candidates)) + ' file(s) \'' + self.outputfile + '*\' found'

    def generate_dom(self):
        tool = bind.tool()
        tool.tool = self.name
        tool.issue = []
        for child in self.children:
            tool.issue.append(child.generate_dom())
        return tool

    def __str__(self):
        result = "ProcessNode (id = " + str(self.node_id) + ")\n\nName: " + self.name +\
                 "\nTerminal Output: " + self.terminal_output +\
                 "\nOutput file: " + self.outputfile + "\nFile Output: " + self.file_output
        return result


class IssueNode(Node):

    def __init__(self, data_graph, severity, url, name, descr, longdescr, fixstr):
        Node.__init__(self, data_graph)
        self.severity = severity
        self.url = url
        self.name = name
        self.descr = descr
        self.longdescr = longdescr
        self.fixstr = fixstr

    def generate_dom(self):
        issue = bind.issue()
        issue.severity = self.severity
        issue.url = self.url
        issue.name = self.name
        issue.descr = self.descr
        issue.longdescr = self.longdescr
        issue.fixstr = self.fixstr
        return issue

    def __str__(self):
        result = "VulnNode (id = " + str(self.node_id) + ")\n\nName: " + self.name + "\nSeverity: " + self.severity +\
                 "\nURL: " + self.url + "\nDescription: " + self.descr + "\nLong Description: " + self.longdescr +\
                 "\nFix: " + self.fixstr
        return result
