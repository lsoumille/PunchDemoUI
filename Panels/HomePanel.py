#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout

from PunchAction import PunchAdmin
from Utils import StringHelper, URLs


class HomePanel(QWidget):

    name = "Home Panel"

    def __init__(self, parent):
        super(HomePanel, self).__init__(parent)
        self.initUI()

    def initUI(self):
        mystr = PunchAdmin.PunchAdmin().getPunchStatus()
        parsedServices = StringHelper.StringHelper().getParsedStatus(mystr)

        grid = QGridLayout()
        self.setLayout(grid)

        positions = [(i, j) for i in range(12) for j in range(1)]

        for pos,serv in zip(positions, parsedServices.keys()):
            if serv == None:
                continue
            lbLine = QLabel(serv, self)
            lbCol = QLabel()
            if parsedServices[serv] == "UP":
                lbCol.setStyleSheet('background-color: green')
            else:
                lbCol.setStyleSheet('background-color:red')
            grid.addWidget(lbLine, pos[0], 0)
            grid.addWidget(lbCol,pos[0], 1)

        self.setGeometry(300, 300, 250, 150)