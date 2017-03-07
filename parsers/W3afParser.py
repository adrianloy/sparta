#!/usr/bin/python

import xml.dom.minidom
from datagraph.node import *

'''this module used to parse w3af xml report'''
__author__ = 'adrian'


class W3afParser(object):

    @staticmethod
    def create_issue_nodes(tool_node):
        data_graph = tool_node.data_graph
        output_file = tool_node.outputfile + '.xml'
        try:
            __dom = xml.dom.minidom.parse(output_file)
            for vul_xml_node in __dom.getElementsByTagName('vulnerability'):
                severity = vul_xml_node.getAttribute('severity')
                url = vul_xml_node.getAttribute('url')
                name = vul_xml_node.getAttribute('name')
                descr = vul_xml_node.getElementsByTagName('description')[0].firstChild.data

                if len(vul_xml_node.getElementsByTagName('long-description')) == 0:
                    longdescr = ''
                else:
                    longdescr = vul_xml_node.getElementsByTagName('long-description')[0].firstChild.data

                if len(vul_xml_node.getElementsByTagName('fix-guidance')) == 0:
                    fixstr = ''
                else:
                    fixstr = vul_xml_node.getElementsByTagName('fix-guidance')[0].firstChild.data

                issue_node = IssueNode(data_graph, severity, url, name, descr, longdescr, fixstr)
                issue_node_id = tool_node.add_child(issue_node)
                data_graph.view.ui.addNodeTo(tool_node.node_id, issue_node_id, name, "issues")
                data_graph.issue_dict[issue_node_id] = issue_node
        except Exception as ex:
            print "\t[-] Parser error! Invalid w3af xml output file!"
            print(str(ex))
            raise
