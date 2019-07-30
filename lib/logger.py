import time,os
from conf.settings import logpath

def logger(func):
    def inner(*args,**kwargs):
        flag = True
        log = '%s : '%time.ctime()
        try:
            log += func(*args,**kwargs)
        except Exception as e:
            flag =False
            log += e.__str__()
        finally:
            writeLog(flag,log,logpath)
    return inner

def writeLog(flag,log,logpath):
    if flag:
        file = os.path.join(logpath,'log')
    else :
        file = os.path.join(logpath,'errlog')
    with open(file,'a') as f:
        f.writelines(log)

