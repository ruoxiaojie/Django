from django.shortcuts import render,redirect,HttpResponse
from app01 import models
from utils.md5 import encrypt

def auth(func):
    def inner(request,*args,**kwargs):
        ck = request.session.get('yyyyyyy')
        if not ck:
            return redirect('/login.html')
        return func(request,*args,**kwargs)
    return inner

@auth
def index(request):
    # 去请求中获取cookie
    # return HttpResponse('登录成功')
    user = request.session.get('yyyyyyy')
    return render(request,'index.html',{'user':user})
@auth
def order(request):
    return HttpResponse('订单列表')

def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        pwd = encrypt(pwd)
        obj = models.UserInfo.objects.filter(username=user,password=pwd).first()
        if obj:
            # 生成随机字符串
            # cookie发送给客户端
            # 服务端随机字符串作为key, 自己设置一些values{}
            request.session['yyyyyyy'] = user
            return redirect('/index.html')
        else:
            return render(request, 'login.html',{'msg':'用户名或密码错误'})

def logout(request):
    request.session.clear()
    return redirect('/login.html')







