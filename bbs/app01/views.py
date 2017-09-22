from django.shortcuts import render,HttpResponse,redirect
from app01 import models
from django.views import View
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.utils.decorators import method_decorator
from utils.md5 import my_md5
from utils.page import Page
from django.forms import Form,fields,widgets
from django import forms
from utils.auth import AuthView

class LoginView(View):
    '''登入'''
    @method_decorator(csrf_exempt) #取消csrf的防御机制
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView,self).dispatch(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        return render(request, 'login.html')

    def post(self,request,*args,**kwargs):
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        pwd = my_md5(pwd)
        obj = models.UserInfo.objects.filter(username=user,password=pwd).first()
        if obj:
            request.session['user_info'] = {'id':obj.id,'username':obj.username}
            return redirect('/index.html')
        return render(request, 'login.html', {'msg': '帐号或密码不正确'})


def index(request):
    return render(request,'index.html')



def logout(request):
    request.session.clear()
    return redirect('/login.html')


