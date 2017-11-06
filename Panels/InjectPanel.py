#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QPushButton

from PunchAction import PunchInject


class InjectPanel(QWidget):

    name = "Inject Panel"

    def __init__(self, parent):
        super(InjectPanel, self).__init__(parent)
        self.client = PunchInject.PunchInject()
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
        buttonStartDdos = QPushButton('Start DDOS Attack', self)
        buttonStartDdos.setToolTip('Click to start DDOS logs')
        buttonStartDdos.clicked.connect(self.client.injectDDOS)
        grid.addWidget(lbLine2, 2, 0)
        grid.addWidget(buttonStartDdos, 3, 0)

        self.setGeometry(300, 300, 250, 150)
