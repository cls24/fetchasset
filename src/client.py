from src import plugins
from concurrent.futures import ThreadPoolExecutor
from gevent import monkey
from gevent.pool import Pool
monkey.patch_all()
class BaseClient(object):

    def getAsset(self):
        return []

    def sendData(self,data):
        pass

    def process(self):
        raise Exception('you must implement this method')

class SSHClient(BaseClient):
    def process(self):
        pass


class SaltClient(BaseClient):

    def process(self):
        hosts = self.getAsset()
        # pool = ThreadPoolExecutor(5)
        pool = Pool(5)

        data = {}

        for h in hosts:
            pool.apply(plugins.pack,h)
        data = {h: plugins.pack(h) for h in hosts}
        self.sendData(data)
