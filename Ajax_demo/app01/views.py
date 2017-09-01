from django.shortcuts import render,HttpResponse
import time
import json
# Create your views here.

def index(request):
    # time.sleep(4)
    return render(request,"index.html")

def sendAjax(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    dic={"flag":False}
    if username=="liu" and password=="1234":
        dic={"flag":True}
    return HttpResponse(json.dumps(dic))

    # d={'name':"xiaojie"}
    # return HttpResponse(json.dumps(d))