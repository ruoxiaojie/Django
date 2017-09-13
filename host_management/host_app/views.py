from django.shortcuts import render,HttpResponse,redirect
from host_app import models
from django.views import View
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.utils.decorators import method_decorator
from utils.md5 import my_md5
from django.forms import Form,fields

class AuthView:
    '''用户认证'''
    def dispatch(self,request,*args,**kwargs):
        if request.session.get('user_info'):
            res = super(AuthView,self).dispatch(request,*args,**kwargs)
            return res
        else:
            return redirect('/login.html')

class UserForm(Form):
    '''生成Form表单'''
    username = fields.CharField(
        max_length=16,
        error_messages={'required':'用户名不能为空'}
    )
    password = fields.CharField(
        max_length=16,
        error_messages={'required':'密码不能为空'}
    )
    email = fields.EmailField(
        max_length=32,
        error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'},
    )
    ip = fields.GenericIPAddressField(
        max_length=16,
        error_messages={'required': 'IP不能为空', 'invalid': 'IP格式错误'}
    )

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

def logout(request):
    request.session.clear()
    return redirect('/login.html')


class IndexView(AuthView,View):
    def get(self,request,*args,**kwargs):
        user_list=models.UserInfo.objects.all()
        return render(request,'index.html',{'user_list':user_list})








# class login()
