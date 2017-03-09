#!/usr/bin/python

from datagraph.node import *
import re

'''this module used to parse hydra console output'''
__author__ = 'adrian'


class HydraParser(object):

    @staticmethod
    def create_issue_nodes(tool_node):
        output = tool_node.terminal_output
        data_graph = tool_node.data_graph
        if 'password: ' in output:
            login = re.findall(r'login: [a-z]+', output)[0]
            pw = re.findall(r'password: [a-z]+', output)[0]
            login = login[7:]
            pw = pw[10:]

            descr = 'Unsafe credentials used'
            longdescr = 'login: ' + login + '\npassword: ' + pw
            severity = '5.0'
            name = 'Unsafe credentials'
            issue_node = IssueNode(data_graph, severity, '', name, longdescr, '', '')
            issue_node_id = tool_node.add_child(issue_node)
            data_graph.view.ui.addNodeTo(tool_node.node_id, issue_node_id, name, "issues")
            data_graph.issue_dict[issue_node_id] = issue_node
