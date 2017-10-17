from django.shortcuts import render,HttpResponse

# Create your views here.
import requests
import time,re,json

def login(req):
    req.method == "GET"
    uuid_time = int(time.time() * 1000)

    base_uuid_url = "https://login.wx.qq.com/" \
                    "jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com" \
                    "%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang" \
                    "=zh_CN&_={0}"
    uuid_url = base_uuid_url.format(uuid_time)
    r1 = requests.get(uuid_url)
    # print(r1.text)
    res=re.findall('= "(.*)";',r1.text)
    # print(res[0])
    uuid = res[0]
    req.session['UUID_TIME'] = uuid_time
    req.session['UUID'] = uuid



    return render(req,'login.html',{'uuid':uuid})

def check_login(req):
    response={'code':408,'data':None}
    ctime = int(time.time()*1000)
    '''htt----VJ5DQlpQ==&tip=1&r=-724936237&_=1508258456655'''
    base_login_url = "https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}&tip=1&r=-724936237&_={1}"
    login_url = base_login_url.format(req.session['UUID'],ctime)
    r1 = requests.get(login_url)
    if 'window.code=408' in r1.text:
        response['code'] = 408
    elif 'window.code=201' in r1.text:
        #扫码成功返回头像
        response['code'] = 201
        response['data'] = re.findall("window.userAvatar = '(.*)';",r1.text)[0]
    return HttpResponse(json.dumps(response))
