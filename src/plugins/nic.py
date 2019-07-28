from src.plugins import base
import salt.client as sc


class NicPlugin(base.BasePlugins):
    def cmd(self,host):
        ret = []
        local = sc.LocalClient()
        grains = local.cmd(host, "grains.items")[host]
        nics = filter(lambda x: x != 'lo', grains['hwaddr_interfaces'].keys())
        for nic in nics:
            name = nic
            hwaddr = grains['hwaddr_interfaces'][nic]
            ipv4 = grains['ip4_interfaces'][nic][0]
            ret.append({'name':name,'hwaddr':hwaddr,'ipv4':ipv4})
        return ret
