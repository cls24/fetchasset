from conf import settings
import importlib
from lib.response import BaseResponse
# def pack(host):
#     package = {}
#     for plugin, v in settings.plugins.items():
#         tmp = {'status':True,'data':None}
#         try:
#             path, cls = v.rsplit(".", 1)
#             p = importlib.import_module(path)
#             tmp['data']=getattr(p,cls)().execute(host)
#         except Exception as e:
#             print(e)
#             tmp['status'] = False
#         package[plugin] = tmp
#         print(tmp)
#     return package

def pack(host):
    package = {}
    for plugin, v in settings.plugins.items():
        try:
            path, cls = v.rsplit(".", 1)
            p = importlib.import_module(path)
            data = getattr(p,cls)().execute(host)
            package[plugin]=data
        except Exception as e:
            resp = BaseResponse()
            resp.status = False
            resp.error = e.__str__()
            package[plugin]=resp
    return package