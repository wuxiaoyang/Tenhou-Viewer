# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
import sys
import os

from about_dialog import about_dialog

class main_window(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        uic.loadUi('./ui/tenhou-viewer.ui',self)

        self.connect(self.action_Exit, SIGNAL('triggered()'), self.slot_Exit)
        self.connect(self.action_About, SIGNAL('triggered()'), self.slot_About)

    def slot_Exit(self):
        
        self.close()
    def slot_About(self):
        w = about_dialog(parent = self)
        w.show()

def __main():
    
    app = QApplication(sys.argv)
    w = main_window()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    __main()
