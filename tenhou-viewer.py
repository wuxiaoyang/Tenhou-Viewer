# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
import sys
import os
import webbrowser

from AboutDialog import AboutDialog

class main_window(QMainWindow):

    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)
        uic.loadUi('./ui/tenhou-viewer.ui',self)
        #self.setAttribute(Qt.WA_QuitOnClose)
        self.connect(self.actionExit, SIGNAL('triggered()'), self.slot_Exit)
        self.connect(self.actionAbout, SIGNAL('triggered()'), self.slot_About)

    def slot_Exit(self):
        self.close()

    def slot_About(self):
        w = AboutDialog(self)
        w.show()

def __main():

    webbrowser.get('windows-default').open('http://www.google.com') 
    app = QApplication(sys.argv)
    w = main_window()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    __main()
