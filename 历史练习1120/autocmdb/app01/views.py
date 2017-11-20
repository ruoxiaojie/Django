
from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http.request import QueryDict

@csrf_exempt
def asset(request):
    if request.method == "GET":
        return HttpResponse('收到:GET')
    else:
        print(request.POST)
        print(request.body.decode('utf-8'))
        return HttpResponse('收到:POST')

def host_list(request):
    print(request.GET,type(request.GET))
    # request.GET._mutable = True

    obj = QueryDict(mutable=True)
    obj['_zhaofengfeng'] = request.GET.urlencode() # page=10&id=1
    url_param = obj.urlencode()

    hosts = ['c1.com','c2.com','c3.com']
    return render(request,'host_list.html',{'hosts':hosts,'url_param':url_param})

def add_host(request):
    if request.method == "GET":
        return render(request,'add.html')
    else:
        url_params = request.GET.get('_zhaofengfeng')
        host = request.POST.get('hostname')
        url ="/host_list.html?"+url_params
        return redirect(url)
