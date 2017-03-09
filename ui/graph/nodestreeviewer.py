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
        self.selection_changed_callback = None
        self.treeWidget.itemSelectionChanged.connect(self.on_selection_changed)

    def set_selection_changed_callback(self, selection_changed_callback):
        self.selection_changed_callback = selection_changed_callback

    def on_selection_changed(self):
        selected_items = self.treeWidget.selectedItems()
        if len(selected_items) == 1 and self.selection_changed_callback:
            self.selection_changed_callback(selected_items[0])

    def clear(self):
        self.treeWidget.clear()

    def build_from(self, data_graph):
        root = self.treeWidget.invisibleRootItem()
        for host_id, host_node in data_graph.host_dict.iteritems():
            host_item = self.add_child(root, host_node.ip + " (" + host_node.name + ")", host_node.node_id)
            self.host_dict[host_id] = host_item
            self.item_dict[host_node.node_id] = host_item

        for port_id, port_node in data_graph.port_dict.iteritems():
            host_item = self.host_dict[data_graph.get_node(port_node.parent_node_id).host_id]
            port_item = self.add_child(host_item, port_node.number + "/" + port_node.protocol + " (" +
                                       port_node.service_name + ")", port_node.node_id)
            self.port_dict[port_id] = port_item
            self.item_dict[port_node.node_id] = port_item

        for tool_id, tool_node in data_graph.tool_dict.iteritems():
            port_item = self.port_dict[data_graph.get_node(tool_node.parent_node_id).port_id]
            tool_item = self.add_child(port_item, tool_node.name, tool_node.node_id)
            self.tool_dict[tool_id] = tool_item
            self.item_dict[tool_node.node_id] = tool_item

        for issue_id, issue_node in data_graph.issue_dict.iteritems():
            tool_item = self.tool_dict[data_graph.get_node(issue_node.parent_node_id).process_id]
            issue_item = self.add_child(tool_item, issue_node.name, issue_node.node_id)
            self.item_dict[issue_node.node_id] = issue_item

    @staticmethod
    def add_child(parent, title, node_id):
        item = QtGui.QTreeWidgetItem(parent, [title])
        item.setData(0, QtCore.Qt.UserRole, node_id)
        return item
