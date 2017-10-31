#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

from Panels.HomePanel import HomePanel
from Panels.InjectPanel import InjectPanel
from Panels.SystemPanel import SystemPanel
from Utils import URLs, SSHHelper


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.client = SSHHelper.SSHHelper()
        self.initUI()

    def initUI(self):
        mainMenu = self.menuBar()
        homeMenu = mainMenu.addMenu('Home')
        punchMenu = mainMenu.addMenu('Punch Commands')
        demoMenu = mainMenu.addMenu('Demo Resources')
        dashMenu = mainMenu.addMenu('Links to Dashboards')

        #Home Menu
        homeButton = QAction(QIcon('exit24.png'), 'Home', self)
        homeButton.setStatusTip('Go to Home Page')
        homeButton.triggered.connect(self.loadHomeCliked)
        homeMenu.addAction(homeButton)

        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        homeMenu.addAction(exitButton)

        #Punch Menu
        adminButton = QAction(QIcon('exit24.png'), 'System commands', self)
        adminButton.setStatusTip('Start/Stop Punchplatform')
        adminButton.triggered.connect(self.loadPunchAdnminCliked)
        punchMenu.addAction(adminButton)

        injectButton = QAction(QIcon('exit24.png'), 'Demo commands', self)
        injectButton.setStatusTip('Inject logs in PunchPlatform')
        injectButton.triggered.connect(self.loadPunchInjectCliked)
        punchMenu.addAction(injectButton)

        #Links To dashboards
        kibanaButton = QAction(QIcon('exit24.png'), 'Kibana', self)
        kibanaButton.setStatusTip('Go to Kibana dashboards')
        kibanaButton.triggered.connect(URLs.goToKibana)
        dashMenu.addAction(kibanaButton)

        grafanaButton = QAction(QIcon('exit24.png'), 'Grafana', self)
        grafanaButton.setStatusTip('Go to Grafana dashboards')
        grafanaButton.triggered.connect(URLs.goToGrafana)
        dashMenu.addAction(grafanaButton)

        punchButton = QAction(QIcon('exit24.png'), 'Punch Admin', self)
        punchButton.setStatusTip('Go to Punch Admin')
        punchButton.triggered.connect(URLs.goToPunchAdmin)
        dashMenu.addAction(punchButton)

        stormButton = QAction(QIcon('exit24.png'), 'Storm UI', self)
        stormButton.setStatusTip('Go to Storm UI')
        stormButton.triggered.connect(URLs.goToStorm)
        dashMenu.addAction(stormButton)

        self.form_widget = HomePanel(self)
        self.setCentralWidget(self.form_widget)

        self.setGeometry(700, 100, 300, 300)
        self.setWindowTitle('PunchDemo UI')
        self.show()

    def loadHomeCliked(self):
        self.form_widget = HomePanel(self)
        self.setCentralWidget(self.form_widget)

    def loadPunchAdnminCliked(self):
        self.form_widget = SystemPanel(self)
        self.setCentralWidget(self.form_widget)
        return

    def loadPunchInjectCliked(self):
        self.form_widget = InjectPanel(self)
        self.setCentralWidget(self.form_widget)
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
