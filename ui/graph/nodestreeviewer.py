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
        self.tool_dict = {}

    def clear(self):
        self.treeWidget.clear()

    def build_from(self, data_graph):
        root = self.treeWidget.invisibleRootItem()
        for host_id, host_node in data_graph.host_dict.iteritems():
            host_item = self.add_child(root, 0, host_node.ip + " (" + host_node.name + ")")
            self.host_dict[host_id] = host_item
            self.item_dict[host_node.node_id] = host_item

        for port_id, port_node in data_graph.port_dict.iteritems():
            host_item = self.host_dict[data_graph.get_node(port_node.parent_node_id).host_id]
            port_item = self.add_child(host_item, 1, port_node.number + "/" + port_node.protocol + " (" + port_node.service_name + ")")
            self.port_dict[port_id] = port_item
            self.item_dict[port_node.node_id] = port_item

        for tool_id, tool_node in data_graph.tool_dict.iteritems():
            port_item = self.port_dict[data_graph.get_node(tool_node.parent_node_id).port_id]
            tool_item = self.add_child(port_item, 2, tool_node.name)
            self.tool_dict[tool_id] = tool_item
            self.item_dict[tool_node.node_id] = tool_item

        for issue_id, issue_node in data_graph.issue_dict.iteritems():
            tool_item = self.tool_dict[data_graph.get_node(issue_node.parent_node_id).process_id]
            issue_item = self.add_child(tool_item, 2, issue_node.name)
            self.item_dict[issue_node.node_id] = issue_item

    @staticmethod
    def add_child(parent, column, title):
        item = QtGui.QTreeWidgetItem(parent, [title])
        item.setData(column, QtCore.Qt.UserRole, True)
        return item
