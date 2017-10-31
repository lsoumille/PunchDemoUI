import re


class StringHelper():

    def getServiceFromStatus(self, str):
        if str:
            return re.findall('[a-zA-Z ]*', str)[0]
        return None

    def getStateFromStatus(self, str):
        if str:
            return re.findall('.*(UP|DOWN)', str)[0]
        return None

    def getParsedStatus(self, mystr):
        tab = str.split(mystr, '\n')
        serviceAndStatus = {}
        for serv in tab:
            serviceAndStatus[self.getServiceFromStatus(serv)] = self.getStateFromStatus(serv)
        return serviceAndStatus
