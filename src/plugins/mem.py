from src.plugins import base
import salt.client as sc
import re
class MemPlugin(base.BasePlugins):
    def salt(self,host):
        local = sc.LocalClient()
        ret = local.cmd(host, 'cmd.run', ['dmidecode |grep -A16 "Memory Device$"'])
        mems = []
        li = ret[host].split('--')
        res = filter(lambda x: len(re.findall('Size: \d+ MB', x)) > 0, li)
        for s in res:
            tmp = {}
            dic = {i.strip().split(':')[0]: i.strip().split(':')[1] for i in filter(lambda x: x, s.split('\n')[2:])}
            tmp['sn'] = dic['Serial Number']
            tmp['slot'] = dic['Locator']
            tmp['vendor'] = dic['Manufacturer']
            tmp['capacity'] = float(dic['Size'].replace('MB','').strip())
            mems.append(tmp)
        return mems

    def ssh(self,host):
        pass