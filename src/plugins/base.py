from conf.settings import mode

class BasePlugins(object):
    def __init__(self):
        self.mode = mode

    def ssh(self,cmd):
        return cmd

    def salt(self,cmd):
        return cmd

    def execute(self,host):
        # if self.mode in {"ssh","salt"}:
        return getattr(self,self.mode)(self.cmd(host))

    def cmd(self,host):
        pass

