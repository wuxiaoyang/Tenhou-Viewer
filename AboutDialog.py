# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import uic

class AboutDialog(QtGui.QWidget):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui =  uic.loadUi('./ui/about.ui')
        self.ui.label_2.setPixmap(QtGui.QPixmap('./resources/shawn.png'))
        self.ui.show()

        #self.setFixedSize(400,200)
