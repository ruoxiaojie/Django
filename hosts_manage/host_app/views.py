from django.shortcuts import render,HttpResponse,redirect
from utils.md5 import my_md5
from host_app import models
# Create your views here.

def auth(func):
    def inner(request,*args,**kwargs):
        # url=request.path ##第一次url
        global url
        ck=request.session.get('uuuuuu')
        if not ck:
            return redirect('/login.html')
        return func(request,*args,**kwargs)
    return inner




def login(request):
    if request.method == 'GET':
        return render(request,"login.html")
    else:
        user=request.POST.get('user')
        pwd=request.POST.get('pwd')
        pwd=my_md5(pwd)
        obj=models.User.objects.filter(username=user,password=pwd).first()
        if not obj:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})
        else:
            request.session['uuuuuu'] = user
            return redirect('/index.html')


#全局url 返回第一次访问url




def logout(request):
    request.session.clear()
    return redirect('/login.html')







#往数据库批量添加数据
# def add(request):
#     for i in range(1,303):
#         username="xiaojie{}".format(i)
#         email="{}@qq.com".format(i)
#         pwd=123456
#         password=my_md5(str(pwd))
#         models.User.objects.create(username=username,email=email,password=password)
#     return HttpResponse('创建成功')


from utils.page import Page
@auth
def user_list(request):

    current_page = request.GET.get('page') #当前页
    try:
        current_page  = int(current_page)
    except Exception as e:
        current_page = int(1)
    all_count = models.User.objects.all().count()     #数据总条数
    page_obj = Page(current_page,all_count,request.path_info) #requ request.path_info当前URL
    user_list = models.User.objects.all()[page_obj.start:page_obj.end]
    page_str = page_obj.page_html()

    return render(request,'user.html',{'user_list':user_list,'page_str':page_str})



@auth
def index(request):

    current_page = request.GET.get('page') #当前页
    try:
        current_page  = int(current_page)
    except Exception as e:
        current_page = int(1)
    all_count = models.Host.objects.all().count()     #数据总条数
    page_obj = Page(current_page,all_count,request.path_info) #requ request.path_info当前URL
    host_list = models.Host.objects.all()[page_obj.start:page_obj.end]
    page_str = page_obj.page_html()

    return render(request,'index.html',{'host_list':host_list,'page_str':page_str})





###批量修改密码
# @auth
# def user_change(request):
#     return HttpResponse("OK")
    # models.User.objects.all().update(password='e10adc3949ba59abbe56e057f20f883e') #修改密码

# def add(request):
#     ip=192.168.1.1
#     port=22
#     models.User.objects.all().update(port=port)
#     return HttpResponse("OK")




