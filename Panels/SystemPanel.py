#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QPushButton

from PunchAction import PunchAdmin


class SystemPanel(QWidget):

    name = "System Panel"

    def __init__(self, parent):
        super(SystemPanel, self).__init__(parent)
        self.client = PunchAdmin.PunchAdmin()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        lbLine = QLabel("Punchplatform Monitoring :", self)
        buttonStartPunch = QPushButton('Start Punchplatform', self)
        buttonStartPunch.setToolTip('Click to start Punchplatform Services')
        buttonStartPunch.clicked.connect(self.client.startPunchPlatform)
        buttonStopPunch = QPushButton('Stop Punchplatform', self)
        buttonStopPunch.setToolTip('Click to stop Punchplatform Services')
        buttonStopPunch.clicked.connect(self.client.stopPunchPlatform)
        grid.addWidget(lbLine, 0, 0)
        grid.addWidget(buttonStartPunch, 1, 0)
        grid.addWidget(buttonStopPunch, 1, 1)

        lbLine2 = QLabel("Channel Monitoring :", self)
        buttonStartChannels = QPushButton('Start Channels', self)
        buttonStartChannels.setToolTip('Click to start log channels')
        buttonStartChannels.clicked.connect(self.client.startChannels)
        buttonStopChannels = QPushButton('Stop Channels', self)
        buttonStopChannels.setToolTip('Click to stop log channels')
        buttonStopChannels.clicked.connect(self.client.stopChannels)
        grid.addWidget(lbLine2, 2, 0)
        grid.addWidget(buttonStartChannels, 3, 0)
        grid.addWidget(buttonStopChannels, 3, 1)

        lbLine3 = QLabel("Clear data :", self)
        buttonClearElastic = QPushButton('Delete all logs', self)
        buttonClearElastic.setToolTip('Click to delete all logs in Elasticsearch')
        buttonClearElastic.clicked.connect(self.client.clearData)
        grid.addWidget(lbLine3, 4, 0)
        grid.addWidget(buttonClearElastic, 5, 0)

        self.setGeometry(300, 300, 250, 150)

