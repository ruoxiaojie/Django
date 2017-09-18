from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# from app01.forms import UserInfoForm
from app01.forms import RegisterForm
def userinfo(request):
    user_list = models.UserInfo.objects.all()
    return render(request,'userinfo.html',{'user_list':user_list})


def add_user(request):
    if request.method == 'GET':
        form = UserInfoForm()
        return render(request,'add_user.html',{'form':form})
    else:
        form = UserInfoForm(data=request.POST)
        if form.is_valid():
            models.UserInfo.objects.create(**form.cleaned_data)
            return redirect('/userinfo/')
        return render(request, 'add_user.html', {'form': form})


def register(request):
    if request.method == "GET":
        # form = RegisterForm(initial={'city':[1,2],'name':'alex'})
        form = RegisterForm()
        return render(request,'register.html',{'form':form})
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['pwd'])
            print(form.cleaned_data['pwd_confirm'])

        return render(request, 'register.html', {'form': form})
