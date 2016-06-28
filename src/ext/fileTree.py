import sys, os
os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Tree(QWidget):
    """ File tree widget for Codex"""
    def __init__(self, parent = None):
        super(Tree, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.fsModel = QtGui.QFileSystemModel()
        # Starting 1 directory higher seems like a good place
        # TODO: Allow user to set a working directory to use for root
        self.fsIndex = self.fsModel.setRootPath(QString(os.path.dirname(os.path.dirname(str(config.filename)))))
        self.treeView = QtGui.QTreeView(self)
        self.treeView.setModel(self.fsModel)
        self.treeView.setDragEnabled(True)
        self.treeView.setDragDropMode(QAbstractItemView.InternalMove)
        self.treeView.setRootIndex(self.fsIndex)
        self.treeView.setAnimated(True)
        self.treeView.setHeaderHidden(True)
        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)
        self.treeView.resize(150,430)
        self.treeView.clicked.connect(self.clicked)

    def clicked(self):
        self.file = self.fsModel.fileName(self.fsIndex)
        config.filename = str(self.file)
        config.m.open()