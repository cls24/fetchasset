from conf import settings
import importlib

def pack(host):
    package = {}
    for plugin, v in settings.plugins.items():
        path,cls = v.rsplit(".",maxsplit=1)
        p = importlib.import_module(path)
        package[plugin]=getattr(p,cls)().execute(host)
    return package
