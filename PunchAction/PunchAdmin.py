import threading

from Utils import Constants
from Utils import SSHHelper
from Utils import URLs


class PunchAdmin:

    def __init__(self):
        super().__init__()
        self.client = SSHHelper.SSHHelper()
        self.client.connectToPunchPlatform()

    def getPunchStatus(self):
        self.client.sendCommand(
            Constants.env_variables + "/home/adm-infra/punchplatform-standalone-3.3.5/bin/punchplatform-admin.sh status")
        return self.client.result

    def startPunchPlatform(self):
        t = threading.Thread(target=self.client.sendCommand, args=(Constants.env_variables + "/home/adm-infra/punchplatform-standalone-3.3.5/bin/punchplatform-admin.sh start",))
        t.start()

    def stopPunchPlatform(self):
        t = threading.Thread(target=self.client.sendCommand, args=(
        Constants.env_variables + "/home/adm-infra/punchplatform-standalone-3.3.5/bin/punchplatform-admin.sh stop",))
        t.start()

    def startChannels(self):
        t = threading.Thread(target=self.client.sendCommand, args=(Constants.env_variables + "/home/adm-infra/punchplatform-standalone-3.3.5/bin/punchplatform-channel.sh --start " + Constants.tenant,))
        t.start()

    def stopChannels(self):
        t = threading.Thread(target=self.client.sendCommand, args=(Constants.env_variables + "/home/adm-infra/punchplatform-standalone-3.3.5/bin/punchplatform-channel.sh --stop " + Constants.tenant,))
        t.start()

    def clearData(self):
        #Get all indices
        indices = URLs.getIndicesFromElastic()
        #delete indices if it's not equal to .kibana
        for indice in indices:
            if indice == '.kibana':
                continue
            t = threading.Thread(target=URLs.deleteIndice, args=(indice,))
            t.start()
        return