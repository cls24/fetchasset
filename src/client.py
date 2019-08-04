from src import plugins
# from concurrent.futures import ThreadPoolExecutor
from gevent import monkey
from gevent.pool import Pool
monkey.patch_all()
import gevent
import requests
import hashlib,time,json
from conf.settings import mykey,url
from lib import logger
from lib.serailize import JsonCustomerEncoder
import salt.client as sc

class BaseClient(object):

    def authkey(self,ctime):
        md5 = hashlib.md5()
        txt = '%s%s' % (mykey, ctime)
        md5.update(txt.encode('utf8'))
        authkey = md5.hexdigest()
        return authkey

    # @logger.logger
    def postData(self,url,data):
        ctime = time.time()
        authkey = self.authkey(ctime)
        key_time = '%s|%s' % (authkey, ctime)
        data = json.dumps(data,cls=JsonCustomerEncoder)
        res = requests.request('post', url=url + authkey, data={'data':data}, headers={"authkey": key_time})
        print(res.text)
        # return res

    def getAsset(self):
        local = sc.LocalClient()
        ret = local.cmd('*', 'test.ping')
        hosts = [k for k,v in ret.items() if v]
        return hosts


    def sendData(self,url,data,pool=5):
        pool = Pool(pool)
        gs = [pool.spawn(self.postData,url,data[h]) for h in data.keys()]
        gevent.joinall(gs)

    def process(self):
        raise Exception('you must implement this method')

class SSHClient(BaseClient):

    def process(self):
        pass

class SaltClient(BaseClient):

    # @logger.logger
    def run(self,hosts,pool_size=5):
        p = Pool(pool_size)
        gs = [p.spawn(plugins.pack,h) for h in hosts]
        gevent.joinall(gs)
        data = {h:g.value for h,g in zip(hosts,gs)}
        return data

    def process(self):
        hosts = self.getAsset()
        # pool = ThreadPoolExecutor(5)
        res = self.run(hosts)
        self.postData(url,res)
        # self.sendData(url,res)
