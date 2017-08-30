from django.shortcuts import render,HttpResponse
import time
import json
# Create your views here.

def index(request):
    # time.sleep(4)
    return render(request,"index.html")

def sendAjax(request):
    d={'name':"xiaojie"}

    return HttpResponse(json.dumps(d))