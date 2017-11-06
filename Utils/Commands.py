from Utils import SSHHelper, Constants, StringHelper

class Commands:

    def getInjectorPids(self):
        client = SSHHelper.SSHHelper()
        client.connectToPunchPlatform()
        test = client.sendCommand(
            Constants.env_variables + "ps ax | grep log-injector")
        return StringHelper.StringHelper().getAllPids(client.result)