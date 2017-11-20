from django.shortcuts import render,HttpResponse,redirect
from host_app import models
from django.views import View
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.utils.decorators import method_decorator
from utils.md5 import my_md5
from utils.page import Page
from django.forms import Form,fields,widgets
from django import forms

class AuthView(View):
    '''用户认证'''
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        if request.session.get('user_info'):
            response = super(AuthView,self).dispatch(request,*args,**kwargs)
            return response
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
        widget=forms.PasswordInput(),
        error_messages={'required':'密码不能为空'}

    )
    email = fields.EmailField(
        max_length=32,
        error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'},
    )

    # ip = fields.GenericIPAddressField(
    #     max_length=16,
    #     error_messages={'required': 'IP不能为空', 'invalid': 'IP格式错误'}
    # )

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
    def get(self, request, *args, **kwargs):
        return render(request,'index.html')


class HostsView(AuthView,View):
    def get(self,request,*args,**kwargs):
        current_page = request.GET.get('page')  # 当前页
        try:
            current_page = int(current_page)
        except Exception as e:
            current_page = int(1)
        all_count = models.HostInfo.objects.all().count()  # 数据总条数
        page_obj = Page(current_page, all_count, request.path_info)  # requ request.path_info当前URL
        host_list = models.HostInfo.objects.all()[page_obj.start:page_obj.end]
        page_str = page_obj.page_html()
        return render(request, 'hosts.html', {'host_list': host_list, 'page_str': page_str})


class GamesView(AuthView,View):
    def get(self,request,*args,**kwargs):
        current_page = request.GET.get('page')  # 当前页
        try:
            current_page = int(current_page)
        except Exception as e:
            current_page = int(1)
        all_count = models.UserHost.objects.all().count()  # 数据总条数
        page_obj = Page(current_page, all_count, request.path_info)  # requ request.path_info当前URL
        game_list = models.UserHost.objects.all()[page_obj.start:page_obj.end]
        page_str = page_obj.page_html()
        return render(request, 'games.html', {'game_list': game_list, 'page_str': page_str})

class UsersView(AuthView,View):
    def get(self,request,*args,**kwargs):
        current_page = request.GET.get('page')  # 当前页
        try:
            current_page = int(current_page)
        except Exception as e:
            current_page = int(1)
        all_count = models.UserInfo.objects.all().count()  # 数据总条数
        page_obj = Page(current_page, all_count, request.path_info)  # requ request.path_info当前URL
        user_list = models.UserInfo.objects.all()[page_obj.start:page_obj.end]
        page_str = page_obj.page_html()
        return render(request, 'users.html', {'user_list': user_list, 'page_str': page_str})



class AddUserView(AuthView,View):
    '''添加用户,利用form表单'''
    def get(self,request,*args,**kwargs):
        form=UserForm()
        return render(request,"adduser.html",{'form':form})
    '''确认添加后POST请求进来'''
    def post(self,request,*args,**kwargs):
        form=UserForm(data=request.POST)
        if form.is_valid():
            obj = models.UserInfo.objects.create(**form.cleaned_data)
            return redirect('/users.html')
        else:
            return render(request,'adduser.html',{'form':form})





class EditUserView(AuthView,View):
    '''用户编辑'''
    def get(self,request,pk):
        obj = models.UserInfo.objects.filter(id=pk).first()
        pass



