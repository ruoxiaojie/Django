from django.shortcuts import render,HttpResponse, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.utils.decorators import method_decorator
from app01 import models

#form
from django.forms import Form,fields,widgets


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
            return redirect('add_user.html')
        return render(request, 'login.html',{'msg': '去你的'})

class UsersView(AuthView,View):

    def get(self,request,*args,**kwargs):
        user_list = models.UserInfo.objects.all()
        return render(request,'users.html',{'user_list':user_list})

class AddUserView(AuthView,View):
    def get(self,request,*args,**kwargs):
        return render(request,'add_user.html')

class UserForm(Form):
    username=fields.CharField(
        #只能输入32个字符
        max_length=32,
        required=True,
        error_messages={'required':'用户不能为空'}
    )

    password=fields.CharField(
        required=True,
        error_messages={'required':'密码不能为空','invalid':'ip格式错误'}
    )
    ut_id=fields.ChoiceField(choices=[])
    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        self.fields['ut_id'].choices=models.UserType.objects.values_list('id','title')

class AddUserView(AuthView,View):
    def get(self,request,*args,**kwargs):
        form=UserForm()
        return render(request,'add_user.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=UserForm(data=request.POST)
        if form.is_valid():
            models.UserInfo.objects.create(**form.cleaned_data)
            return redirect('/users.html')
        else:
            print(form.errors)
            return render(request,'add_user.html',{'form':form})

class EditUserView(AuthView,View):
    def get(self,request,pk):
        obj=models.UserInfo.objects.filter(id=pk).first()
        form=UserForm(initial={'username':obj.username,'password':obj.password,'ut_id':obj.ut_id})
        return render(request,'edit_user.html',{'form':form})


    def post(self,request,pk):
        form=UserForm(data=request.POST)
        if form.is_valid():
            models.UserInfo.objects.filter(id=pk).update(**form.cleaned_data)
            return redirect('/users.html')
        else:
            print(form.errors)
            return render(request,'edit_user.html',{'form':form})


class DelUserView(AuthView,View):
    def get(self,pk):
        models.UserInfo.objects.filter(id=pk).delete()
        return redirect('/users.html')








