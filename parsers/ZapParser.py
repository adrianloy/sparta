import xml_bindings.zap as bind
from datagraph.node import *


class ZAPParser(object):

    def __init__(self, process_node):
        self.process_node = process_node
        self.data_graph = process_node.data_graph

    def process(self, output):
        scan = bind.CreateFromDocument(output)
        for result in scan.result:
            vuln = VulNode(self.data_graph, '', '', '', result.name, '', '')
            self.process_node.add_child(vuln)

output = open('zap_output.xml', 'r').read()
scan = bind.CreateFromDocument(output)