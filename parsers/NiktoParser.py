from datagraph.node import *
import untangle


class NiktoParser(object):

    @staticmethod
    def create_issue_nodes(tool_node):
        data_graph = tool_node.data_graph

        if tool_node.file_output == '':
            print 'process_file_output is empty'
            return

        scan = untangle.parse(tool_node.file_output)
        for item in scan.niktoscan.scandetails.item:
            # TODO: improve issue node data
            name = 'NiktoIssue'
            issue_node = IssueNode(data_graph, '', '', name, item.description.cdata, '', '')
            # port_node = data_graph.get_node(process_node.parent_node_id)
            issue_node_id = tool_node.add_child(issue_node)
            data_graph.view.ui.addNodeTo(tool_node.node_id, issue_node_id, name, "issues")
            data_graph.issue_dict[issue_node_id] = issue_node
