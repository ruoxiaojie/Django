from django.shortcuts import render,HttpResponse,redirect
from utils.md5 import my_md5
from host_app import models
# Create your views here.





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






def index(request):
    return render(request,'index.html')

def logout(request):

    return redirect('/login.html')






'''
#往数据库批量添加数据
def name(request):
    for i in range(1,303):
        username="xiaojie{}".format(i)
        pwd=123456
        password=my_md5('pwd')
        models.User.objects.create(username=username,password=password)
    return HttpResponse('创建成功')
    '''

from utils.page import Page
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





