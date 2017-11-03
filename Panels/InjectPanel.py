#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QPushButton

import PunchAction


class InjectPanel(QWidget):

    name = "Inject Panel"

    def __init__(self, parent):
        super(InjectPanel, self).__init__(parent)
        self.client = PunchAction.PunchInject.PunchInject()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        lbLine = QLabel("Noise :", self)
        buttonStartInjection = QPushButton('Start Noise Injection', self)
        buttonStartInjection.setToolTip('Click to start Noise Injection')
        buttonStartInjection.clicked.connect(self.client.injectNoise)
        buttonStopInjection = QPushButton('Stop Noise Injection', self)
        buttonStopInjection.setToolTip('Click to stop Noise Injection')
        buttonStopInjection.clicked.connect(self.client.stopNoise)
        grid.addWidget(lbLine, 0, 0)
        grid.addWidget(buttonStartInjection, 1, 0)
        grid.addWidget(buttonStopInjection, 1, 1)

        lbLine2 = QLabel("DDOS scenario :", self)
        buttonStartChannels = QPushButton('Start DDOS Attack', self)
        buttonStartChannels.setToolTip('Click to start DDOS logs')
        grid.addWidget(lbLine2, 2, 0)
        grid.addWidget(buttonStartChannels, 3, 0)

        self.setGeometry(300, 300, 250, 150)
