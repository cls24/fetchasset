from conf.settings import mode

class BasePlugins():
    def __init__(self):
        self.mode = mode

    def ssh(self,cmd):
        return cmd

    def salt(self,cmd):
        return cmd

    def execute(self):
        if self.mode in {"ssh","salt"}:
            return getattr(self,self.mode)(self.cmd())
        else:
            raise Exception("invaild mode,please check the settings file")
    def cmd(self):
        pass

