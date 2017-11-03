import webbrowser
import pycurl
from io import BytesIO

from Utils import Constants, StringHelper


def goToKibana(self):
    webbrowser.open_new_tab(Constants.kibana)


def goToGrafana(self):
    webbrowser.open_new_tab(Constants.grafana)


def goToPunchAdmin(self):
    webbrowser.open_new_tab(Constants.punch_admin)


def goToStorm(self):
    webbrowser.open_new_tab(Constants.storm_ui)

def getIndicesFromElastic():
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, Constants.elastic_indices)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    body = buffer.getvalue()
    return StringHelper.StringHelper().getAllIndiceNames(body.decode())

def deleteIndice(indice):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, Constants.elastic + "/" + indice)
    c.setopt(pycurl.CUSTOMREQUEST, "DELETE")
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    body = buffer.getvalue()
    return body.decode()
