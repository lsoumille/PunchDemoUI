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
        self.client.connect(Constants.punchplatform_ip, Constants.ssh_port, Constants.account, Constants.password)

    def sendCommand(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        self.result = stdout.read().decode("utf-8")
        print(self.result)
        print(stderr.read)
        return str(stdout.read())