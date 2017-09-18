from django.shortcuts import render,HttpResponse,redirect
from app01 import models
from app01.forms import UserInfoForm


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



def login(request):
    return render(request,'login.html')

def test(request):
    print('test')
    return HttpResponse('ok')


