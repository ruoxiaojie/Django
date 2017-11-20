from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.
from app01.forms import UserInfoForm

def userinfo(request):
    user_list = models.UserIofo.objects.all()
    return render(request,'userinfo.html',{'user_list':user_list})

def add_user(request):
    if request.method == 'GET':
        form = UserInfoForm()
        return render(request,'add_user.html',{'form':form})
    else:
        form =UserInfoForm(data=request.POST)
        if form.is_valid():
            models.UserIofo.objects.create(**form.cleaned_data)
            return redirect('/userinfo/')

        return render(request,'add_user.html',{'form':form})