import threading

from Utils import Constants
from Utils import FileHelper
from Utils import SSHHelper


class PunchInject:

    def __init__(self):
        super().__init__()
        self.client = SSHHelper.SSHHelper()
        self.client.connectToPunchPlatform()

    def injectNoise(self):
        self.client.sendCommand(
            Constants.env_variables + Constants.noise_path)
        #Save PID for each injection process to kill them if wished
        pids = str.split(self.client.result, '\n')
        print(pids)
        FileHelper.FileHelper().saveToPIDFile(pids[1:len(pids)])
        return

    def stopNoise(self):
        #Get PID from .pid and kill them
        pids = FileHelper.FileHelper().getSavedPids()
        for pid in pids:
            t = threading.Thread(target=self.client.sendCommand, args=(Constants.env_variables + "kill -9 " + pid,))
            t.start()
        return

    def injectDDOS(self):
        return