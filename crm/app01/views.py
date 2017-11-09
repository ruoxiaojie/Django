from django.shortcuts import render,HttpResponse,redirect
from django.forms import Form,fields,widgets
from rbac import models
class LoginForm(Form):
    username = fields.CharField(required=True,error_messages={'required':"用户名不能为空"})
    password = fields.CharField(required=True,error_messages={'required':"密码不能为空"})


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request,'login.html',{'form':form})
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            #用户名密码通过认证  去数据库检测用户是否存在
            # models.UserInfo.objects.filter(username=form.cleaned_data['user'],password=form.cleaned_data['pwd'])
            user = models.UserInfo.objects.filter(**form.cleaned_data).first()
            if user:
                #role_list=user.roles,all()
                role_list=user.roles.values(
                    'title',
                    'permissions__title',
                    'permissions__url',
                    'permissions__code',
                    'permissions__group',
                    'permissions__is_menu',
                ).distinct()
                print(role_list)
                return HttpResponse('ok')

                return redirect('/index/')
            else:
                # form.add_error("password","用户名或密码错误") #lowb
                from django.core.exceptions import ValidationError
                form.add_error("password", ValidationError("用户名或密码错误"))

        return render(request, 'login.html', {'form': form})