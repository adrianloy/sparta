from datagraph.node import *
import untangle


class ZapParser(object):

    @staticmethod
    def create_vuln_nodes(process_node):
        data_graph = process_node.data_graph

        if process_node.process_file_output == '':
            print 'process_file_output is empty'
            return

        scan = untangle.parse(process_node.process_file_output)
        for issue in scan.zap.issue:
            try:
                # TODO: improve vuln node data
                name = 'ZapIssue'
                vuln_node = VulNode(data_graph, '', '', name, issue.description.cdata, '', '')
                # port_node = data_graph.get_node(process_node.parent_node_id)
                vuln_node_id = process_node.add_child(vuln_node)
                data_graph.view.ui.addNodeTo(process_node.node_id, vuln_node_id, name, "vulnerabilities")
                data_graph.vul_dict[vuln_node_id] = vuln_node
            except IndexError:
                pass
