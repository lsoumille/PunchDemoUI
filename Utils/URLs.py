import webbrowser

from Utils import Constants


def goToKibana(self):
    webbrowser.open_new_tab(Constants.kibana)


def goToGrafana(self):
    webbrowser.open_new_tab(Constants.grafana)


def goToPunchAdmin(self):
    webbrowser.open_new_tab(Constants.punch_admin)


def goToStorm(self):
    webbrowser.open_new_tab(Constants.storm_ui)