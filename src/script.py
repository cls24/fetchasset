from conf import settings
from src import client

def run():
    if settings.mode=='ssh':
        cli = client.SSHClient()
    elif settings.mode=='salt':
        cli = client.SaltClient()
    else:
        raise Exception("invaild mode,please check the settings file")
    cli.process()