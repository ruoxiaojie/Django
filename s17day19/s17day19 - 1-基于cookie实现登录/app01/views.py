from django.shortcuts import render,redirect,HttpResponse
from app01 import models
from utils.md5 import encrypt
def index(request):
    # 去请求中获取cookie
    ck = request.COOKIES.get('uuuuuuuuu')
    if not ck:
        return redirect('/login.html')
    return HttpResponse('登录成功')


def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        pwd = encrypt(pwd)
        obj = models.UserInfo.objects.filter(username=user,password=pwd).first()
        if obj:
            # 在用户口袋中放一个凭证(响应头中)
            response = redirect('/index.html')
            response.set_cookie('uuuuuuuuu',user)
            # response.set_cookie('uuuuuuuuu1',user)
            return response
        else:
            return render(request, 'login.html',{'msg':'用户名或密码错误'})