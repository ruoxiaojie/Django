from django.shortcuts import render,HttpResponse,redirect
from app01 import models
import hashlib
# Create your views here.


def encrypt(pwd):
    obj=hashlib.md5()
    obj.update(pwd.encoding('utf-8'))
    data=obj.hexdigest()
    return data

def auth(func): #登入装饰器
    def inner(request,*args,**kwargs):
        ck = request.session.get('yyyyyy')
        if not ck:

         return func(request,*args,**kwargs)
    return inner



def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        user=request.POST.get('user')
        pwd=request.POST.get('pwd')
        pwd=encrypt(pwd)
        obj=models.user.objects.filter(username=user,password=pwd).first()



    return HttpResponse("登入成功")





def index(request):
    user=request.session.get('yyyyyy')
    return render(request,'home.html',{'user':user})

