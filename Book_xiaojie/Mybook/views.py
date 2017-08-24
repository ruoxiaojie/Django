from django.shortcuts import render,HttpResponse,redirect
# from Mybook.models import

# Create your views here.

def index(request):
    # return HttpResponse("okokokokokoko")
    return render(request,"base.html")
