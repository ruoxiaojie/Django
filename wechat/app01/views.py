from django.shortcuts import render,HttpResponse

# Create your views here.
import requests
import time,re

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


