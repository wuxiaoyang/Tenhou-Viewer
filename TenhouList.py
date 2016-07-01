# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import uic

class TenhouList(QtGui.QTableWidget):

    def __init__(self, parent = None):

        QtGui.QTableWidget.__init__(self, parent)
        self.setColumnCount(5)
        self.setRowCount(5)
        self.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem("Address"))
        self.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem("Function"))
        self.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem("Line"))
