from django.shortcuts import render,HttpResponse,redirect
from app01 import models
from utils import md5
# Create your views here.


# def auth(func):
#     def inner():
#         return func
#     return inner

def auth(func):
    def inner(request,*args,**kwargs):
        ck = request.COOKIES.get('uuuuuu')
        if not ck:
            return redirect('/login')
        return func(request,*args,**kwargs)
    return inner


@auth
def index(request):
    #请求获取cookie
        # user=request.session.get('uuuuuu')
    return render(request, 'index.html')
    # return render(request, 'index.html',{'user':user})


def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        user=request.POST.get('user')
        pwd=request.POST.get('pwd')
        pwd=md5.my_md5(pwd)
        obj = models.UserInfo.objects.filter(username=user,password=pwd).first()


        if not obj:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})
        else:

            request.session['uuuuuu'] = user
            return redirect('/index')
            # response = redirect('/index')
            # #cookie
            # response.set_cookie('uuuuuu',user)
            # return response

@auth
def order(request):
    return HttpResponse("登入成功")

def logout(request):
    request.session.clear()
    return redirect('/login')

def csrf(request):
    return render(request,'csrf.html')

def test(request):
    return render(request,'test.html',{"a":123})