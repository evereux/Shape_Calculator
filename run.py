#! python3
#
# created by Paul Bourne - evereux@gmail.com
# ==========================================

import sys

from PyQt4 import QtGui

from application.gui import CalculateApp

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = CalculateApp()
    app.exec_()

sys.exit(1)
