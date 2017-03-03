from PyQt4 import QtCore, QtGui


class NodesTreeViewer(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.treeWidget = QtGui.QTreeWidget()
        self.treeWidget.setHeaderHidden(True)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.treeWidget)
        self.setLayout(layout)
        self.host_dict = {}
        self.port_dict = {}
        self.item_dict = {}
        self.process_dict = {}

    def clear(self):
        self.treeWidget.clear()

    def build_from(self, data_graph):
        root = self.treeWidget.invisibleRootItem()
        for host_id, host_node in data_graph.host_dict.iteritems():
            host_item = self.add_child(root, 0, host_node.host_ip + " (" + host_node.host_name + ")")
            self.host_dict[host_id] = host_item
            self.item_dict[host_node.node_id] = host_item

        for port_id, port_node in data_graph.port_dict.iteritems():
            host_item = self.host_dict[data_graph.get_node(port_node.parent_node_id).host_id]
            port_item = self.add_child(host_item, 1, port_node.port_number + "/" + port_node.port_protocol + " (" + port_node.standard_service_name + ")")
            self.port_dict[port_id] = port_item
            self.item_dict[port_node.node_id] = port_item

        for process_id, process_node in data_graph.process_dict.iteritems():
            port_item = self.port_dict[data_graph.get_node(process_node.parent_node_id).port_id]
            process_item = self.add_child(port_item, 2, process_node.process_name)
            self.process_dict[process_id] = process_item
            self.item_dict[process_node.node_id] = process_item
            item = self.add_child(process_item, 3, '')
            label = QtGui.QLabel(process_node.process_terminal_output)
            label.setWordWrap(True)
            self.treeWidget.setItemWidget(item, 0, label)

        for vuln_id, vuln_node in data_graph.vul_dict.iteritems():
            process_item = self.process_dict[data_graph.get_node(vuln_node.parent_node_id).process_id]
            vuln_item = self.add_child(process_item, 2, vuln_node.name)
            self.item_dict[vuln_node.node_id] = vuln_item
            item = self.add_child(vuln_item, 3, '')
            label = QtGui.QLabel(vuln_node.longdescr)
            label.setWordWrap(True)
            self.treeWidget.setItemWidget(item, 0, label)

    def add_child(self, parent, column, title):
        item = QtGui.QTreeWidgetItem(parent, [title])
        item.setData(column, QtCore.Qt.UserRole, True)
        return item
