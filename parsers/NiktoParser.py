from datagraph.node import *
import untangle


class NiktoParser(object):

    @staticmethod
    def create_vuln_nodes(process_node):
        data_graph = process_node.data_graph

        if process_node.process_file_output == '':
            print 'process_file_output is empty'
            return

        scan = untangle.parse(process_node.process_file_output)
        for item in scan.niktoscan.scandetails.item:
            # TODO: improve vuln node data
            name = 'NiktoIssue'
            vuln_node = VulNode(data_graph, '', '', name, item.description.cdata, '', '')
            port_node = data_graph.get_node(process_node.parent_node_id)
            vuln_node_id = port_node.add_child(vuln_node)
            data_graph.view.ui.addNodeTo(port_node.node_id, vuln_node_id, name, "vulnerabilities")
            data_graph.vul_dict[vuln_node_id] = vuln_node
