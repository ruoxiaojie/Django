from django.shortcuts import render,redirect,HttpResponse
from my_mamager.models import *
import json
from utils.md5 import make_md5
from utils.myutils import BaseReponse
from my_mamager import forms
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def p_add(request):
    for i in range(5,333):
        HostInfo.objects.create(name='s%s.adsys.zzzc.qihoo.net'%(i),ip='1.1.1.%s' %(i),port=22,service_line_id='2' )
    return HttpResponse('ok')

def auth(func):
    '''判断是否登录装饰器'''
    def inner(request,*args,**kwargs):
        v = request.session.get('user')
        if not v:
            return redirect('/login.html')
        return func(request, *args,**kwargs)
    return inner

def login(request):
    my_response = BaseReponse()
    if request.method == 'POST':
        obj = forms.LoginForm(request.POST)
        if obj.is_valid():
            username = request.POST.get('username')
            password = make_md5(request.POST.get('password'))
            if UserInfo.objects.filter(username=username,password=password).count():
                my_response.status = True
                request.session['user'] = username
                return HttpResponse(json.dumps(my_response.__dict__,ensure_ascii=False))
            else:
                my_response.status = False
                my_response.error = {'error_msg':["用户名或密码错误,请重新输入"]}
                return HttpResponse(json.dumps(my_response.__dict__,ensure_ascii=False))
        else:
            print(obj.errors['username'][0])
            print(obj.errors['password'][0])
            my_response.error = obj.errors
            return HttpResponse(json.dumps(my_response.__dict__,ensure_ascii=False))
    return render(request,'login.html')


def logout(request):
    request.session.clear()
    return redirect('/login.html')

@auth
def index(request):
    '''首页'''
    if request.method == 'GET':
        host_list = HostInfo.objects.all().select_related('service_line')
        service_list = ServiceLine.objects.all()
        page = request.GET.get('page', 1)
        currentPage = int(page)
        host_list, p_range,total_num = parse(host_list, page)
        path = request.path_info
        return render(request,'base.html',locals())


def parse(host_list,page):
    '''分页'''
    paginator = Paginator(host_list, 7)
    total_num = int(paginator.num_pages)
    currentPage = int(page)
    if currentPage <= 4:
        p_range = paginator.page_range[0:7]
    elif currentPage > 4 and currentPage < total_num - 3:
        p_range = paginator.page_range[currentPage - 3 - 1:currentPage + 3]
    else:
        p_range = paginator.page_range[total_num - 7:total_num]
    try:
        host_list = paginator.page(page)
    except PageNotAnInteger:
        host_list = paginator.page(1)
    except EmptyPage:
        host_list = paginator.page(paginator.num_pages)
    return host_list,p_range,total_num



def register(request):
    '''注册'''
    if request.method == 'POST':
        my_response = BaseReponse()
        obj = forms.RegisterForm(request.POST)
        if obj.is_valid():
            pwd = make_md5(request.POST.get('password'))
            UserInfo.objects.create(username=request.POST.get('username'),password=pwd,email=request.POST.get('email'))
            my_response.status = True
            return HttpResponse (json.dumps(my_response.__dict__,ensure_ascii=False))
        else:
            my_response.error = obj.errors
            return HttpResponse(json.dumps(my_response.__dict__,ensure_ascii=False))
    else:
        return render(request,'register.html')


def check_login_user(request):
    """检测用户是否存在"""
    if request.method == 'POST':
        my_response = BaseReponse()
        if UserInfo.objects.filter(username=request.POST.get('logname')).count():
            my_response.status = True
            return HttpResponse(json.dumps(my_response.__dict__,ensure_ascii=False))
        else:
            my_response.status = False
            return HttpResponse(json.dumps(my_response.__dict__,ensure_ascii=False))
@auth
def show_manager(request,id):
    """查看产品线对应都管理人员"""
    service_obj = ServiceLine.objects.get(id=id).userinfo_set.all()

    return render(request,'show_manager.html',locals())

@auth
def modify(request):
    """修改操作"""
    if request.method == 'POST':
        my_response = BaseReponse()
        obj = forms.ModifyForm(request.POST)
        if obj.is_valid():
            res_dic = {}
            user_dic = request.POST
            for k,v in dict(user_dic).items():
                if k  == 'id':
                    continue
                else:
                    if k == 'hostname':
                        res_dic['name'] = v[0]
                    elif k == 'service':
                        res_dic['service_line_id'] = v[0]
                    else:
                        res_dic[k] = v[0]
            my_response.status = True
            HostInfo.objects.filter(id=request.POST.get('id')).update(**res_dic)
            data = HostInfo.objects.filter(id=request.POST.get('id')).values('name','port','ip','service_line__name','service_line_id')
            my_response.data = data[0]
            return HttpResponse(json.dumps(my_response.__dict__, ensure_ascii=False))
        else:
            my_response.error = obj.errors
            return HttpResponse(json.dumps(my_response.__dict__, ensure_ascii=False))

@auth
def delete(request):
    """删除操作"""
    if request.method == 'POST':
        my_response = BaseReponse()
        id = request.POST.get('id')
        HostInfo.objects.filter(id=id).delete()
        my_response.status = True
    return HttpResponse(json.dumps(my_response.__dict__, ensure_ascii=False))

@auth
def add(request):
    """添加操作"""
    my_response = BaseReponse()
    if request.method == 'POST':
        obj = forms.ModifyForm(request.POST)
        if obj.is_valid():
            msg_dic = request.POST
            HostInfo.objects.create(name=msg_dic.get('hostname'),ip=msg_dic.get('ip'),port=msg_dic.get('port'),service_line_id=msg_dic.get('service_line_id'))
            my_response.status = True
            return HttpResponse(json.dumps(my_response.__dict__, ensure_ascii=False))
        else:
            my_response.error = obj.errors
            return HttpResponse(json.dumps(my_response.__dict__, ensure_ascii=False))
    if request.method == 'GET':
        service_list = ServiceLine.objects.all()
        return render(request,'add.html',locals())
@auth
def search(request):
    '''搜索功能'''
    if request.method == 'POST':
        service_list = ServiceLine.objects.all()
        if request.POST.get('search_title', None):
            '''创建一个数据库存放上次搜索状态,供分页使用'''
            Searchpoint.objects.all().delete()
            Searchpoint.objects.create(name=request.POST.get('search_title'))
            host_list =HostInfo.objects.filter(name__icontains=request.POST.get('search_title')).select_related('service_line')
            page = request.GET.get('page', 1)
            currentPage = int(page)
            host_list, p_range, total_num = parse(host_list, page)
            return render(request, 'search.html', locals())
        else:
            Searchpoint.objects.all().delete()
            return redirect('/index.html')
    if request.method == 'GET':
        service_list = ServiceLine.objects.all()
        if Searchpoint.objects.all().count():
            host_list = HostInfo.objects.filter(name__icontains=Searchpoint.objects.values('name').first()['name']).select_related('service_line')
            page = request.GET.get('page', 1)
            currentPage = int(page)
            host_list, p_range, total_num = parse(host_list, page)
            return render(request, 'search.html', locals())

@auth
def check_host(request):
    """检测用户是否存在重复"""
    if request.method == 'POST':
        my_response = BaseReponse()
        if HostInfo.objects.filter(name=request.POST.get('hostname')).count():
            my_response.status = True
            return HttpResponse(json.dumps(my_response.__dict__,ensure_ascii=False))
        else:
            my_response.status = False
            return HttpResponse(json.dumps(my_response.__dict__,ensure_ascii=False))

@auth
def check_service(request):
    """检测业务线是否存在重复"""
    if request.method == 'POST':
        my_response = BaseReponse()
        if ServiceLine.objects.filter(name=request.POST.get('service_name')).count():
            my_response.status = True
            return HttpResponse(json.dumps(my_response.__dict__,ensure_ascii=False))
        else:
            my_response.status = False
            return HttpResponse(json.dumps(my_response.__dict__,ensure_ascii=False))

@auth
def add_service(request):
    """添加业务线"""
    my_response = BaseReponse()
    if request.method == 'POST':
        obj = forms.ServiceForm(request.POST)
        if obj.is_valid():
            msg_dic = request.POST
            ServiceLine.objects.create(name=msg_dic.get('name'))
            obj = ServiceLine.objects.get(name=msg_dic.get('name'))
            obj.userinfo_set.add(*msg_dic.getlist('manager'))
            my_response.status = True
            return HttpResponse(json.dumps(my_response.__dict__, ensure_ascii=False))
        else:
            my_response.error = obj.errors
            return HttpResponse(json.dumps(my_response.__dict__, ensure_ascii=False))
    if request.method == 'GET':
        user_list = UserInfo.objects.all()
        return render(request,'add_service.html',locals())


