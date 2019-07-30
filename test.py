import requests
import hashlib,json,time

def test():
    url = 'http://127.0.0.1:8000/api/'
    data = {'data':'asdasd'}
    md5 = hashlib.md5()
    ctime = time.time()
    txt = '%s%s' %(mykey,ctime)
    md5.update(bytes(txt, encoding='utf8'))
    authkey = md5.hexdigest()
    key_time = '%s|%s' %(authkey,ctime)
    print(authkey)
    res = requests.request('post',url=url+authkey,data=json.dumps(data),headers={"authkey":key_time})
    print('one',res.text)
    res = requests.request('post', url=url+authkey, data='asdasd', headers={"authkey": key_time})
    print('two', res.text)
    time.sleep(8)
    res = requests.request('post', url=url+authkey, data='asdasd', headers={"authkey": key_time})
    print('two',res.text)
    res = requests.request('post', url=url+authkey, data='asdasd', headers={"authkey": '%s|%s' %(authkey,time.time())})
    print('two',res.text)

from gevent import monkey
from gevent.pool import Pool
import gevent
# monkey.patch_all()
import random

def run(func,m,n,pool_size=10):
    p = Pool(pool_size)
    g = [p.spawn(func,i,j) for i,j in zip(m,n)]
    gevent.joinall(g)
    return map(lambda x:x.value,g)

def creatTask(func,*arg,**kwargs):
    return func(*arg,**kwargs)

if __name__ == '__main__':
    def func(n,m):
        gevent.sleep(1)
        return n+m
    n = []
    m = []
    for i in range(100):
        n.append(random.randint(1,100))
        m.append(random.randint(1,100))
    res = run(func,m,n,pool_size=50)
    print([*res])
    # test()