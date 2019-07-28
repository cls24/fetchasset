from src import plugins

class BaseClient(object):
    def getHost(self):
        return []

    def sendData(self,data):
        pass


class SSHClient(BaseClient):
    def process(self):
        pass

class SaltClient(BaseClient):

    def process(self):
        hosts = self.getHost()
        data = {h: plugins.pack(h) for h in hosts}
        self.sendData(data)
