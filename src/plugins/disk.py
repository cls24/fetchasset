from src.plugins import base

class Diskplugin(base.BasePlugins):
    def cmd(self):
        return "disk info"