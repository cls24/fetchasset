from src.plugins import base
import salt.client as sc


class ServerPlugin(base.BasePlugins):
    def salt(self,host):
        local = sc.LocalClient()
        grains = local.cmd(host, "grains.items")
        server_info = {}
        for i in grains.keys():
            server_info['hostname'] = grains[i]["nodename"]
            server_info['sn'] = grains[i]["serialnumber"]
            server_info['vendor'] = grains[i]["manufacturer"]
            server_info['os_platform'] = grains[i]["osfullname"]
            server_info['os_version'] = grains[i]["osmajorrelease"]
            server_info['cpu_cores'] = grains[i]["num_cpus"]
            server_info['cpu_model'] = grains[i]["cpu_model"]
        return server_info

    def ssh(self,host):
        pass