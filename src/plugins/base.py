from conf.settings import mode
from lib.response import BaseResponse

class BasePlugins(object):
    def __init__(self):
        self.mode = mode

    def ssh(self,host):
        raise Exception('you must implement this method')

    def salt(self,host):
        raise Exception('you must implement this method')

    def execute(self,host):
        resp = BaseResponse()
        try:
            resp.data = getattr(self,self.mode)(host)
        except Exception as e:
            resp.status = False
            resp.error = e
        return resp
