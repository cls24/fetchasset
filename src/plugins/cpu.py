from src.plugins import base


class Cpuplugin(base.BasePlugins):
    def cmd(self):
        return "cpu info"

if __name__ == '__main__':
    c = Cpuplugin()
    ret = c.execute()
    print(ret)