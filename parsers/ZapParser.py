from datagraph.node import *
import untangle


class ZapParser(object):

    @staticmethod
    def create_issue_nodes(tool_node):
        data_graph = tool_node.data_graph

        if tool_node.file_output == '':
            print 'process_file_output is empty'
            return

        scan = untangle.parse(tool_node.file_output)
        for issue in scan.zap.issue:
            try:
                # TODO: improve issue node data
                name = 'ZapIssue'
                issue_node = IssueNode(data_graph, '', '', name, issue.description.cdata, '', '')
                # port_node = data_graph.get_node(process_node.parent_node_id)
                issue_node_id = tool_node.add_child(issue_node)
                data_graph.view.ui.addNodeTo(tool_node.node_id, issue_node_id, name, "issues")
                data_graph.issue_dict[issue_node_id] = issue_node
            except IndexError:
                pass
