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

    def getAllIndiceNames(self, indices):
        tab = str.split(indices, '\n')
        indices = []
        for line in tab:
            if line == '':
                continue
            indices.append(str.split(line, ' ')[2])
        return indices

    def getAllPids(self, pids):
        tab = str.split(pids, '\n')
        allpids = []
        for line in tab:
            if line == '':
                continue
            fields = str.split(line, ' ')
            if fields[0] == '' and fields[1] != '':
                allpids.append(fields[1])
            elif fields[0] != '':
                allpids.append(fields[0])
        return allpids

