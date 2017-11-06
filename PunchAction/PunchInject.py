import threading

from Utils import Constants
from Utils import FileHelper
from Utils import SSHHelper
from Utils import StringHelper
from Utils import Commands


class PunchInject:

    def __init__(self):
        super().__init__()
        self.client = SSHHelper.SSHHelper()
        self.client.connectToPunchPlatform()

    def injectNoise(self):
        t = threading.Thread(target=self.client.sendCommand, args=(Constants.env_variables + Constants.noise_path,))
        t.start()
        return

    def stopNoise(self):
        #Get PID by sending ps command ans kill them
        pids = Commands.Commands().getInjectorPids()
        for pid in pids:
            if pid == '':
                continue
            t = threading.Thread(target=self.client.sendCommand, args=(Constants.env_variables + "kill -9 " + pid,))
            t.start()
        return

    def injectDDOS(self):
        t = threading.Thread(target=self.client.sendCommand, args=(Constants.env_variables + Constants.ddos_path,))
        t.start()
        return