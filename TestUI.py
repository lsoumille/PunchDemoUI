#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we position two push
buttons in the bottom-right corner
of the window.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
import Constants
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

import SSHHelper


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.client = SSHHelper.SSHHelper()
        self.initUI()

    def initUI(self):
        #SSHHelper.SSHHelper.connectToPunchPlatform(self.client)
        #print(SSHHelper.SSHHelper.sendCommand(self.client, Constants.env_variables + "/home/adm-infra/punchplatform-standalone-3.3.5/bin/punchplatform-admin.sh status"))

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
