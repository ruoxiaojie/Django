from django.shortcuts import render,HttpResponse

# Create your views here.
import time

from django.views.decorators.cache import cache_page

# @cache_page(10) #缓存10秒
def test1(request):
    ctime =time.time()
    return render(request,'test1.html',{'ctime':ctime})

def test2(request):
    ctime =time.time()
    return render(request,'test2.html',{'ctime':ctime})


def md(request):
    print('views.md')
    return HttpResponse("MD")