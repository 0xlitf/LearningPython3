import smt_new_pb2
import test_pb2
import sys
import tarfile
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QRegExp
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTreeView, QPushButton, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel,
                             QLineEdit, QFileDialog, QMenu, QAction, QMessageBox,
                             QAbstractItemView, QHeaderView, QStyleFactory)
from image_view import GraphicsView


class FilterModel(QSortFilterProxyModel):
    def __init__(self, parent):
        super(FilterModel, self).__init__(parent)
        self.parent = parent

    def update(self):
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        # print('filterAcceptsRow', source_row)
        reg = self.filterRegExp()
        if reg.isEmpty():
            return True

        reg.setCaseSensitivity(Qt.CaseInsensitive)
        current = self.sourceModel().index(source_row, 0, source_parent)
        name = current.data()
        value = current.siblingAtColumn(1).data()

        if reg.indexIn(name) != -1:
            return True
        elif reg.indexIn(value) != -1:
            return True
        else:
            children = self.sourceModel().rowCount(current)
            for k in range(children):
                if self.filterAcceptsRow(k, current) is True:
                    return True

        return False


class TreeView(QMainWindow):
    def __init__(self, parent=None):
        super(TreeView, self).__init__(parent)
        self.setWindowTitle('Protobuf Viewer')
        # 设置表头信息
        self.model = QStandardItemModel(self)
        self.model.setHorizontalHeaderLabels(['Name', 'Value'])

        self.findItems = []
        self.findIndex = 0

        # self.proxy = FilterModel(self)
        # self.proxy.setSourceModel(self.model)
        # self.proxy.setFilterKeyColumn(-1)
        # self.proxy.setRecursiveFilteringEnabled(True)
        # self.proxy.setSortCaseSensitivity(Qt.CaseInsensitive)
        # self.proxy.setDynamicSortFilter(True)
        # self.proxy.sort(0)

        tree_view = QTreeView(self)
        # tree_view.setEditTriggers(QAbstractItemView.NoEditTriggers)

        tree_view.setModel(self.model)
        # 调整第一列的宽度
        tree_view.header().resizeSection(0, 300)
        # 设置成有虚线连接的方式
        tree_view.setStyle(QStyleFactory.create('windows'))
        # 完全展开
        tree_view.expandAll()

        # 显示选中行的信息
        tree_view.selectionModel().currentChanged.connect(self.on_current_changed)
        tree_view.setSelectionMode(QAbstractItemView.SingleSelection)
        tree_view.setContextMenuPolicy(Qt.CustomContextMenu)
        tree_view.customContextMenuRequested.connect(self.open_menu)
        tree_view.header().setSectionResizeMode(QHeaderView.Stretch)

        self.treeView = tree_view

        load_btn = QPushButton('Load Template')
        load_btn.clicked.connect(self.load_pb)

        load_annotation_btn = QPushButton('Load Annotation')
        load_annotation_btn.clicked.connect(self.load_annotation_pb)

        load_tpl_btn = QPushButton('Load Template Detail PB')
        load_tpl_btn.clicked.connect(self.load_template_pb)

        h_box1 = QHBoxLayout()
        h_box1.addWidget(load_btn)
        h_box1.addWidget(load_annotation_btn)
        h_box1.addWidget(load_tpl_btn)
        h_box1.addStretch()

        line_edit = QLineEdit()
        line_edit.setClearButtonEnabled(True)
        self.line_edit = line_edit
        line_edit.textChanged.connect(self.on_search_changed)
        search = QPushButton('Search')
        search.clicked.connect(self.on_search)

        h_box2 = QHBoxLayout()
        h_box2.addWidget(line_edit)
        h_box2.addWidget(search)

        v_box = QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addWidget(tree_view)
        widget = QWidget()
        widget.setLayout(v_box)
        self.setCentralWidget(widget)

    def dump_object(self, obj, parent_item):
        for descriptor in obj.DESCRIPTOR.fields:
            value = getattr(obj, descriptor.name)
            if descriptor.type == descriptor.TYPE_MESSAGE:
                root = QStandardItem(descriptor.name)
                col = QStandardItem('')
                parent_item.appendRow([root, col])
                if descriptor.label == descriptor.LABEL_REPEATED:
                    i = 0
                    for item in value:
                        index = QStandardItem('[{}]'.format(i))
                        root.appendRow(index)
                        i += 1
                        self.dump_object(item, index)
                    col.setText('[{}]'.format(i))
                else:
                    self.dump_object(value, root)
            elif descriptor.type == descriptor.TYPE_ENUM:
                for tmp in descriptor.enum_type.values:
                    if tmp.index == value:
                        name_index = QStandardItem(descriptor.name)
                        name_index.setData(tmp.name)
                        value_index = QStandardItem(tmp.name)
                        parent_item.appendRow([name_index, value_index])
            elif descriptor.type == descriptor.TYPE_BYTES:
                name_index = QStandardItem(descriptor.name)
                value_index = QStandardItem('bytes[{}]'.format(len(value)))
                value_index.setData(value)
                parent_item.appendRow([name_index, value_index])
            else:
                name_index = QStandardItem(descriptor.name)
                name_index.setData(str(value))
                value_index = QStandardItem(str(value))
                parent_item.appendRow([name_index, value_index])

    def load_pb(self):
        print("load_pb")
        self.model.setRowCount(0)
        path = QFileDialog.getOpenFileName(self, 'Select Template File', '', "Template (*.proj *.bak *.tmp *.res)")

        if path[0] == '':
            return

        self.setWindowTitle('Protobuf Viewer-' + path[0])
        try:
            tar = tarfile.open(path[0], 'r')
            tar.extractall('./')

            detail_file_name = './detail.tmpl.pb'
            overview_file_name = './overview.tmpl.pb'

            root = QStandardItem('Template')

            overview = QStandardItem('Overview')
            detail = QStandardItem('Detail')
            root.appendRow(overview)
            root.appendRow(detail)

            self.model.appendRow(root)

            f1 = open(overview_file_name, "rb")
            overviewObj = test_pb2.TemplateOverview()
            overviewObj.ParseFromString(f1.read())
            self.dump_object(overviewObj, overview)
            f1.close()

            f2 = open(detail_file_name, "rb")
            detailObj = test_pb2.LoginResponse()
            detailObj.ParseFromString(f2.read())
            self.dump_object(detailObj, detail)
            f2.close()
        except IOError:
            print("Could not open file.")

        self.treeView.expandAll()

    def load_annotation_pb(self):
        print("load_annotation_pb")
        self.model.setRowCount(0)
        path = QFileDialog.getOpenFileName(self, 'Select Annotation File', '', "Annotation (*.nproj)")

        if path[0] == '':
            return

        self.setWindowTitle('Protobuf Viewer-' + path[0])
        try:
            tar = tarfile.open(path[0], 'r')
            tar.extractall('./')

            annotation_file_name = './annotation.pb'

            root = QStandardItem('Annotation')

            self.model.appendRow(root)

            f1 = open(annotation_file_name, "rb")
            obj = smt_new_pb2.PbData()
            obj.ParseFromString(f1.read())
            self.dump_object(obj, root)
            f1.close()
        except IOError:
            print("Could not open file.")

        self.treeView.expandAll()

    def load_template_pb(self):
        print("load_template_pb")
        self.model.setRowCount(0)
        path = QFileDialog.getOpenFileName(self, 'Select Template PB File', '', "PB (*.pb)")
        print("path[0]: ", path[0])
        if path[0] == '':
            return

        self.setWindowTitle('Protobuf Viewer-' + path[0])

        root = QStandardItem('Template')

        self.model.appendRow(root)

        f2 = open(path[0], "rb")
        detailObj = test_pb2.LoginResponse()
        detailObj.ParseFromString(f2.read())
        self.dump_object(detailObj, root)
        f2.close()

        try:
            pass
        except IOError:
            print("Could not open file.")

        self.treeView.expandAll()

    def on_search(self):
        txt = self.line_edit.text()
        # self.proxy.setFilterRegExp(txt)
        # self.treeView.expandAll()

        if len(self.findItems) == 0:
            items1 = self.model.match(self.model.index(0, 0), Qt.DisplayRole, txt, -1, Qt.MatchRecursive)
            items2 = self.model.match(self.model.index(0, 0), Qt.UserRole + 1, txt, -1, Qt.MatchRecursive)
            self.findItems = items1 + items2
            print('findItems', len(self.findItems))
            self.findIndex = 0

        if self.findIndex < len(self.findItems):
            index = self.findItems[self.findIndex]
            if index.isValid():
                self.findIndex += 1
                self.treeView.setCurrentIndex(index)
                self.treeView.scrollTo(index, QAbstractItemView.PositionAtCenter)
            else:
                self.findIndex = 0
                QMessageBox.information(self, 'info', "already at the end!")
        else:
            self.findIndex = 0
            QMessageBox.information(self, 'info', "already at the end!")

    def on_search_changed(self, txt):
        print("on_search_changed", txt)
        self.findItems = []
        self.findIndex = 0

    def open_menu(self, position):
        index = self.treeView.currentIndex()

        if not index.isValid():
            return

        datas = index.data(Qt.UserRole + 1)
        if not datas:
            return

        menu = QMenu()
        action = QAction('Export')
        action.triggered.connect(self.on_export)
        view = QAction('View As Image')
        view.triggered.connect(self.on_view)
        menu.addAction(action)
        menu.addAction(view)
        menu.exec_(self.treeView.viewport().mapToGlobal(position))

    def on_export(self):
        index = self.treeView.currentIndex()

        if not index.isValid():
            return

        datas = index.data(Qt.UserRole + 1)
        if not datas:
            return

        path = QFileDialog.getSaveFileName()
        if path[0] == '':
            return

        try:
            f = open(path[0], 'wb')
            f.write(datas)
            f.close()
        except IOError:
            print("Could not open file.")

    def on_view(self):
        index = self.treeView.currentIndex()

        if not index.isValid():
            return

        datas = index.data(Qt.UserRole + 1)
        if not datas:
            return

        img = QPixmap()
        img.loadFromData(datas)
        if img.isNull():
            return

        self.imgView = GraphicsView()
        self.imgView.setWindowTitle('Image Viewer')
        self.imgView.resize(800, 800)
        self.imgView.load(img)
        self.imgView.show()

    def on_current_changed(self, current, previous):
        txt = str(current.data())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TreeView()
    window.showMaximized()
    sys.exit(app.exec())
