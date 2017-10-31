import paramiko

from Utils import Constants


class SSHHelper:

    result = ""

    def __init__(self):
        super().__init__()
        self.client = paramiko.SSHClient()

    def connectToPunchPlatform(self):
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.WarningPolicy)

        self.client.connect("192.168.1.91", 22, "adm-infra", "azerty")

    def sendCommand(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        self.result = stdout.read().decode("utf-8")
        print("SEND Command :" + stdout.read().decode("utf-8"))
        return str(stdout.read())

    def getPunchStatus(self):
        self.connectToPunchPlatform()
        print("PunchSTATUS : " + self.sendCommand(
            Constants.env_variables + "/home/adm-infra/punchplatform-standalone-3.3.5/bin/punchplatform-admin.sh status"))
        print(self.result)
        return self.result