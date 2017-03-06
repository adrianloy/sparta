#!/usr/bin/python

import xml.dom.minidom
from datagraph.node import *

'''this module used to parse w3af xml report'''
__author__ = 'adrian'


class W3afParser(object):

    @staticmethod
    def create_vuln_nodes(process_node):
        data_graph = process_node.data_graph
        output_file = process_node.process_outputfile + '.xml'
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

                vuln_node = IssueNode(data_graph, severity, url, name, descr, longdescr, fixstr)
                vuln_node_id = process_node.add_child(vuln_node)
                data_graph.view.ui.addNodeTo(process_node.node_id, vuln_node_id, name, "vulnerabilities")
                data_graph.vul_dict[vuln_node_id] = vuln_node
        except Exception as ex:
            print "\t[-] Parser error! Invalid w3af xml output file!"
            print(str(ex))
            raise
