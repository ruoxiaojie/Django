from django.shortcuts import render,HttpResponse


# Create your views here.
def login_in(request):
    if request.method=="POST":
        usname=request.POST.get("user")
        password=request.POST.get("pwd")
        if usname=="liujie" and password=="123":
            return HttpResponse("登入成功")
    return render(request,"login_in.html")