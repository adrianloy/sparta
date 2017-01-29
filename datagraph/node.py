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

    def __str__(self):
        result = "Node (id = " + str(self.node_id) + ")"
        return result


class HostNode(Node):

    def __init__(self, data_graph, host_id, host_ip, host_name):
        Node.__init__(self, data_graph)
        self.host_id = host_id
        self.host_ip = host_ip
        self.host_name = host_name
        self.portNodeDict = {}

    def add_child(self, child):
        if type(child) is PortNode:
            self.portNodeDict[child.port_number] = child
        return Node.add_child(self,child)

    def generate_dom(self):
        host = bind.host()
        host.ip = self.host_ip
        host.hostname = self.host_name
        host.port = []
        for child in self.children:
            host.port.append(child.generate_dom())
        return host

    def __str__(self):
        result = "HostNode (id = " + str(self.node_id) + ")\n\nIP: " + self.host_ip + "\nHostname: " + self.host_name
        return result


class PortNode(Node):

    def __init__(self, data_graph, port_id, port_number, standard_service_name, port_protocol):
        Node.__init__(self, data_graph)
        self.port_id = port_id
        self.port_number = port_number
        self.port_protocol = port_protocol
        self.standard_service_name = standard_service_name

    def generate_dom(self):
        port = bind.port()
        port.number = self.port_number
        port.standardService = self.standard_service_name
        port.issue = []
        port.vuln = []
        port.protocol = self.port_protocol
        for child in self.children:
            if type(child) is VulNode:
                port.vuln.append(child.generate_dom())
            if type(child) is ProcessNode:
                port.issue.append(child.generate_dom())
        return port

    def __str__(self):
        result = "PortNode (id = " + str(self.node_id) + ")\n\nNumber: " + self.port_number + "\nProtocol: " + self.port_protocol + "\nStandard Service: " + self.standard_service_name
        return result


class ProcessNode(Node):

    def __init__(self, data_graph, process_id, process_name, process_output, process_outputfile):
        Node.__init__(self, data_graph)
        self.process_id = process_id
        self.process_name = process_name
        self.process_output = process_output
        self.process_outputfile = process_outputfile

    def generate_dom(self):
        process = bind.process()
        process.tool = self.process_name
        process.output = self.process_output
        process.outputfile = self.process_outputfile
        return process

    def __str__(self):
        result = "ProcessNode (id = " + str(self.node_id) + ")\n\nName: " + self.process_name + "\nOutput: " + self.process_output + "\nOutputfile: " + self.process_outputfile
        return result


class VulNode(Node):

    def __init__(self, data_graph, severity, url,name, descr, longdescr, fixstr):
        Node.__init__(self, data_graph)
        self.severity = severity
        self.url = url
        self.name = name
        self.descr = descr
        self.longdescr = longdescr
        self.fixstr = fixstr

    def generate_dom(self):
        vuln = bind.vuln()
        vuln.severity = self.severity
        vuln.url = self.url
        vuln.name = self.name
        vuln.descr = self.descr
        vuln.longdescr = self.longdescr
        vuln.fixstr = self.fixstr
        return vuln

    def __str__(self):
        result = "VulnNode (id = " + str(self.node_id) + ")\n\nName: " + self.name + "\nSeverity: " + self.severity + "\nURL: " + self.url + "\nDescription: " + self.descr + "\nLong Description: " + self.longdescr + "\nFix: " + self.fixstr
        return result
