import threading

from Utils.SSHHelper import SSHHelper
from Utils import Constants

class PunchInject:

    def __init__(self):
        super().__init__()
        self.client = SSHHelper.SSHHelper()
        self.client.connectToPunchPlatform()

    def injectNoise(self):
        return

    def stopNoise(self):
        return

    def injectDDOS(self):
        return