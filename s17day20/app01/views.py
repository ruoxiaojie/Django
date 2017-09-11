from django.shortcuts import render,HttpResponse, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.utils.decorators import method_decorator
from app01 import models


class AuthView(object):
    def dispatch(self, request, *args, **kwargs):
        if request.session.get('user_info'):
            response = super(AuthView,self).dispatch(request, *args, **kwargs)
            return response
        else:
            return redirect('/login.html')
# FBV、CBV
class LoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView,self).dispatch(request, *args, **kwargs)

    def get(self, request, *args,**kwargs):
        return render(request,'login.html')

    def post(self,request, *args,**kwargs):
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        obj = models.UserInfo.objects.filter(username=user,password=pwd).first()
        if obj:
            request.session['user_info'] = {'id':obj.id,'username': obj.username}
            return redirect('/users.html')
        return render(request, 'login.html',{'msg': '去你的'})

class UsersView(AuthView,View):

    def get(self,request,*args,**kwargs):
        user_list = models.UserInfo.objects.all()
        return render(request,'users.html',{'user_list':user_list})

from django.forms import Form
from django.forms import fields
from django.forms import widgets

class UserForm(Form):
    username = fields.CharField(
        required=True,
        error_messages={'required':'用户名不能为空'},
        widget=widgets.TextInput(attrs={'class':'form-control'})
    )
    password = fields.CharField(
        required=True,
        error_messages={'required': '邮箱不能为空','invalid':'邮箱格式错误'},
        widget = widgets.TextInput(attrs={'class': 'form-control'})
    )
    # fields.EmailField()
    # fields.GenericIPAddressField(protocol='ipv4')

    ut_id = fields.ChoiceField(
        choices=[],
        widget=widgets.Select(attrs={'class':'form-control'})
    )

    role_id = fields.MultipleChoiceField(
        choices=[],
        widget=widgets.SelectMultiple(attrs={'class':'form-control'})
    )

    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        # self.fields已经有所有拷贝的字段
        self.fields['ut_id'].choices = models.UserType.objects.values_list('id','title')
        self.fields['role_id'].choices = models.Role.objects.values_list('id','caption')

class AddUserView(AuthView,View):
    def get(self,request,*args,**kwargs):
        form = UserForm()
        return render(request,'add_user.html',{'form':form})

    def post(self,request,*args,**kwargs):
        form = UserForm(data=request.POST)
        # 将用户提交的数据和UserForm中定义规则进行匹配：
        if form.is_valid():
            # 把所有正确数据获取到
            # {'username': 'xxxxx', 'password': 'xxxxx', 'ut_id': '1'}
            # print(form.cleaned_data)
            # {'username': 'xxxxx', 'password': 'xxxxx', 'ut_id': '1',role_id:}
            role_id_list = form.cleaned_data.pop('role_id') # [1,2]
            obj = models.UserInfo.objects.create(**form.cleaned_data)
            obj.rl.add(*role_id_list)
            return redirect('/users.html')
        else:
            print(form.errors)
            return render(request, 'add_user.html', {'form': form})

class EditUserView(AuthView,View):
    def get(self,request,pk):
        obj = models.UserInfo.objects.filter(id=pk).first()
        role_id_list = obj.rl.values_list('id')
        v = list(zip(*role_id_list))[0] if role_id_list else []
        form = UserForm(initial={'username': obj.username, 'password': obj.password, 'ut_id': obj.ut_id,'role_id':v})
        return render(request,'edit_user.html',{'form':form})

    def post(self,request,pk):
        form = UserForm(data=request.POST)
        if form.is_valid():
            # # {'username': 'xxxxx', 'password': 'xxxxx', 'ut_id': '1',role_id:}
            role_id = form.cleaned_data.pop('role_id')
            # 用户表更新
            query = models.UserInfo.objects.filter(id=pk)
            query.update(**form.cleaned_data)
            obj = query.first()
            obj.rl.set(role_id)

            return redirect('/users.html')
        else:
            print(form.errors)
            return render(request, 'edit_user.html', {'form': form})

class DelUserView(AuthView,View):
    def get(self,request,pk):
        models.UserInfo.objects.filter(id=pk).delete()
        return redirect('/users.html')


# ########################### 注册功能 #################################

class RegisterForm(Form):
    user = fields.CharField(required=True,min_length=6,max_length=18)
    email = fields.EmailField(required=True,min_length=6,max_length=18)
    password = fields.CharField(min_length=12)
import json

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request,'register.html',{'form':form})
    else:
        response = {'status': True,'data': None,'msg':None}
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # 数据库中添加一条数据
            # return redirect('/login.html') # ajax跳转，错错错
        else:
            response['status'] = False
            response['msg'] = form.errors
        return HttpResponse(json.dumps(response))
























