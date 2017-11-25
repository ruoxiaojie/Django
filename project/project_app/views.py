from django.shortcuts import render,redirect,HttpResponse,render_to_response
from utils.md5 import my_md5
from utils.auth import Auth

from django.views.decorators.csrf import csrf_exempt,csrf_protect
from . import models
from django.forms import Form,fields,widgets
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        # request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        pwd = my_md5(pwd)
        obj = models.User.objects.filter(user=user,pwd=pwd).first()
        if obj:
            request.session['user_info']={'id':obj.id,'user':obj.user}
            return redirect('/index')
        return render(request, 'login.html', {'msg': '帐号或密码不正确'})

def logout(request):
    request.session.clear()
    return redirect('/login.html')


@Auth
def index(request):
    return render(request,'index.html')

