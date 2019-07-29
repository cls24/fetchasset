import requests
import hashlib,json,time
mykey = 'zjkassj32jk3iosakjas8928173kklas2'
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

if __name__ == '__main__':
    test()