class BaseResponse(object):
    def __init__(self):
        self.message = None
        self.status = True
        self.data = None
        self.error = None