from django.shortcuts import render,HttpResponse,redirect
from django.forms import Form,fields,widgets
from rbac import models
from rbac.service.init_permission import init_permission
import re
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
                init_permission(request,user)
                return redirect('/index/')
            else:
                # form.add_error("password","用户名或密码错误") #lowb
                from django.core.exceptions import ValidationError
                form.add_error("password", ValidationError("用户名或密码错误"))

        return render(request, 'login.html', {'form': form})

def index(request):
    # 当前请求url
    current_request_url = request.path_info
    # 获取session中保存的权限信息
    from django.conf import settings
    permission_dict = request.session.get(settings.XX)
    if not permission_dict:
        return HttpResponse('未登入')
    flag = False
    for group_id, values in permission_dict.items():
        for url in values['urls']:  # 正则的url
            if re.match(url, current_request_url):
                flag = True
                break
        if flag:
            break
    if not flag:
        return HttpResponse('没有权限访问')

    return HttpResponse('欢迎登入')













