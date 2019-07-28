from conf import settings
from src import client

def run():
    if settings.mode=='ssh':
        client.SSHClient().process()
    elif settings.mode=='salt':
        client.SaltClient().process()
    else:
        raise Exception("invaild mode,please check the settings file")