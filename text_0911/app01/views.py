from django.shortcuts import render,HttpResponse,redirect
from app01 import models
from django.views import View
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.utils.decorators import method_decorator

# Create your views here.

class AuthView:
    '''用户认证'''
    def dispatch(self,request,*args,**kwargs):
        if request.session.get('user_info'):
            res = super(AuthView,self).dispatch(request,*args,**kwargs)
            return res
        else:
            return redirect('/login')

class LoginView(View):
    '''登入'''
    @method_decorator(csrf_exempt) #取消csrf的防御机制
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView,self).dispatch(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        return render(request,'login.html')

    def post(self,request,*args,**kwargs):
        user=request.POST.get('user')
        pwd=request.POST.get('pwd')
        obj=models.UserInfo.objects.filter(username=user,password=pwd).first()
        if obj:
            request.session['user_info'] = {'id':obj.id,'username':obj.username}
            # return redirect('add_user.html')
            return redirect('/users')
        return render(request,'login.html',{'msg':'帐号或密码错误'})


class UsersView(AuthView,View):
    def get(self,request,*args,**kwargs):
        user_list = models.UserInfo.objects.all()
        return render(request,'users.html',{'user_list':user_list})



from django.forms import Form
from django.forms import fields
from django.forms import widgets

class UserForm(Form):
    '''生成form表单'''
    username = fields.CharField(
        min_length=4,
        max_length=16,
        error_messages={'required':'用户名不能为空'},
        # error_messages={'required': '邮箱不能为空','invalid':'邮箱格式错误'}, 格式错误范例 比如邮箱 ip

    )
    password = fields.CharField(
        min_length=2,
        max_length=8,
        error_messages={'required':'密码不能为空',}
    )
    ut_id = fields.ChoiceField(
        choices=[]
    )
    role_id = fields.MultipleChoiceField(
        choices=[]
    )
    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        # self.fields已经有所有拷贝的字段
        self.fields['ut_id'].choices = models.UserType.objects.values_list('id','title')
        self.fields['role_id'].choices = models.Role.objects.values_list('id','caption')




class AddUserView(AuthView,View):
    '''添加记录'''
    def get(self,request,*args,**kwargs):
        form = UserForm()
        return render(request, 'add_user.html', {'form': form})

    def post(self,request,*args,**kwargs):
        form = UserForm(data=request.POST) #post请求
        if form.is_valid(): #{'username': 'xxxxx', 'password': 'xxxxx', 'ut_id': '1',role_id:}
            role_id_list=form.cleaned_data.pop('role_id') # [1,2]
            obj=models.UserInfo.objects.create(**form.cleaned_data)
            obj.rl.add(*role_id_list)
            return redirect('/users')
        else:
            print(form.errors)
            return render(request,'add_user.html',{'form': form})

class EditUserView(AuthView,View):
    '''编辑按钮'''
    def get(self,request,pk):
        obj = models.UserInfo.objects.filter(id=pk).first()
        role_id_list = obj.rl.values_list('id')
        v = list(zip(*role_id_list))[0] if role_id_list else [] #role_id
        form = UserForm(initial={'username':obj.username,'password':obj.password,'ut_id':obj.ut_id,'role_id':v})
        return render(request, 'edit_user.html', {'form': form})
    def post(self,request,pk):
        form = UserForm(data=request.POST)
        if form.is_valid():
            role_id = form.cleaned_data.pop('role.id')
            query = models.UserInfo.objects.filter(id=pk)
            query.update(**form.cleaned_data)
            obj = query.first()
            obj.rl.set(role_id)
            return redirect('/users')
        else:
            print(form.errors)
            return render(request,'edit_user.html',{'form':form})

class DelUserView(AuthView,View):
    def get(self,request,pk):
        models.UserInfo.objects.filter(id=pk).delete()
        return redirect('/users')























