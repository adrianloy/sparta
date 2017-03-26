from datagraph.node import *
import untangle


class ZapParser(object):

    @staticmethod
    def create_issue_nodes(tool_node):
        data_graph = tool_node.data_graph

        if tool_node.file_output == '':
            print 'tool file output is empty'
            return

        scan = untangle.parse(tool_node.file_output)
        for issue in scan.zap.issue:
            try:
                issue_node = IssueNode(data_graph, '', issue.name.cdata, issue.description.cdata, issue.other.cdata,
                                       issue.solution.cdata)
                issue_node_id = tool_node.add_child(issue_node)
                data_graph.view.ui.addNodeTo(tool_node.node_id, issue_node_id, issue.name.cdata, "issues")
                data_graph.issue_dict[issue_node_id] = issue_node
            except IndexError:
                pass
