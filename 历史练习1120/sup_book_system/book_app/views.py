from django.shortcuts import render,HttpResponse,redirect
from book_app.models import *
# Create your views here.

# def index(request):
#     # return HttpResponse("ok")
#     return render(request,"index.html")

def index(request):
    if request.method=="POST":
        return HttpResponse("注册成功")
    return render(request,"index0821.html")