from django.shortcuts import render,HttpResponse,redirect
from book_app.models import *
# Create your views here.

def index(request):
    # return HttpResponse("ok")
    return render(request,"index.html")