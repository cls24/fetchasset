from json import JSONEncoder
from lib import response
import json

class JsonCustomerEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o,response.BaseResponse):
            return o.__dict__
        return JSONEncoder.default(self,o)

if __name__ == '__main__':
    resp = response.BaseResponse()
    print(json.dumps(resp,cls=JsonCustomerEncoder))