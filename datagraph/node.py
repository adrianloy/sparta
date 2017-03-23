import xml_bindings.aggregation as bind
import os.path
import glob
import datagraph

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

    def generate_xml_binding_instance(self):
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
        self.os = []
        self.portNodeDict = {}

    def add_child(self, child):
        if type(child) is PortNode:
            self.portNodeDict[child.number] = child
        return Node.add_child(self, child)

    def generate_xml_binding_instance(self):
        #export the os with highest accuracy:
        max = 0
        maxos = None
        for os in self.os:
            if os.accuracy > max:
                maxos = os
                max = os.accuracy
        host = bind.host()
        host.ip = self.ip
        host.hostname = self.name
        if maxos:
            host.os = datagraph.DataGraph.OS_obj_stringrepr(maxos)
        else:
            host.os = "No OS information available"
        host.port = []
        for child in self.children:
            host.port.append(child.generate_xml_binding_instance())
        return host

    def __str__(self):
        osstring = "\n\nOS detection information:\n"
        for os in self.os:
            osstring += datagraph.DataGraph.OS_obj_stringrepr(os)
        result = "HostNode\n\nIP:\n" + self.ip + "\n\nHostname:\n" + self.name +osstring
        return result


class PortNode(Node):

    def __init__(self, data_graph, port_id, port_number, service_name, port_protocol):
        Node.__init__(self, data_graph)
        self.port_id = port_id
        self.number = port_number
        self.protocol = port_protocol
        self.service_name = service_name

    def generate_xml_binding_instance(self):
        port = bind.port()
        port.number = self.number
        port.standardService = self.service_name
        port.tool = []
        port.protocol = self.protocol
        for child in self.children:
            port.tool.append(child.generate_xml_binding_instance())

        return port

    def __str__(self):
        result = "PortNode\n\nNumber:\n" + self.number + "\n\nProtocol:\n" + self.protocol
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

    def generate_xml_binding_instance(self):
        tool = bind.tool()
        tool.tool = self.name
        tool.issue = []
        for child in self.children:
            tool.issue.append(child.generate_xml_binding_instance())
        return tool

    def __str__(self):
        result = "ToolNode\n\nName:\n" + self.name
        return result


class IssueNode(Node):

    def __init__(self, data_graph, severity, name, descr, misc, fixstr):
        Node.__init__(self, data_graph)
        self.severity = severity
        self.name = name
        self.descr = descr
        self.misc = misc
        self.fixstr = fixstr

    def generate_xml_binding_instance(self):
        issue = bind.issue()
        issue.severity = self.severity
        issue.name = self.name
        issue.descr = self.descr
        issue.misc = self.misc
        issue.fixstr = self.fixstr
        return issue

    def __str__(self):
        result = "IssueNode\n\nName:\n" + self.name + "\n\nDescription:\n" + self.descr + "\n\nMisc.:\n" + self.misc
        return result
