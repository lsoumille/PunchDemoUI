import paramiko
import Constants

class SSHHelper:

    def __init__(self):
        super().__init__()
        self.client = paramiko.SSHClient()

    def connectToPunchPlatform(self):
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.WarningPolicy)

        self.client.connect("192.168.1.91", 22, "adm-infra", "azerty")

    def sendCommand(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        print(stdout.read())
        print(stderr.read())
        return stdout.read()

