from django.shortcuts import render,redirect,HttpResponse
from app01.models import *
# Create your views here.


def ck(request):
    print(request.COOKIES)
    obj= render(request,'ck.html')
    obj.set_cookie('nnn','123123')
    return obj

def login(request):
    if request.method=="GET":
        return render(request,'login.html',{'msg':""})
    else:
        u=request.POST.get('user')
        p=request.POST.get('pwd')
        ct=user.objects.filter(name=u,password=p).count()
        if ct:
            obj=redirect('/home/')
            # obj.set_cookie('uuuuuu',u,max_age=1800)
            #生成随机字符串 发给客户端 保存在服务端  在服务端写入用户名 密码
            request.session['user']=u
            request.session['pwd']=p
            return obj
        else:
            return render(request,'login.html',{'msg':'用户名或密码错误'})

def home(request):
    v=request.session.get('user')
    if v:
        return render(request,'home.html')
    else:
        return redirect('/login/')

def logout(request):
    request.session.clear()
    return redirect('/login/')




def csrf(request):

    return render(request,"csrf.html")




