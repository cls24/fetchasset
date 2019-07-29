from conf import settings
import importlib

def pack(host):
    package = {}
    for plugin, v in settings.plugins.items():
        tmp = {'status':True,'data':None}
        try:
            path, cls = v.rsplit(".", maxsplit=1)
            p = importlib.import_module(path)
            tmp['data']={plugin:getattr(p,cls)().execute(host)}
        except Exception as e:
            tmp['status'] = False
        package[plugin] = tmp
    return package
