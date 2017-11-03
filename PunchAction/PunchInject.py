from Utils import SSHHelper
from Utils import Constants
from Utils.FileHelper import FileHelper


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
        FileHelper.saveToPIDFile(pids[1:len(pids)])
        return self.client.result

    def stopNoise(self):
        return

    def injectDDOS(self):
        return