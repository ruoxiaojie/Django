from django.shortcuts import render,redirect,HttpResponse
from django.db.models import F
from app01.models import *
import json
import os
from utils.md5 import encrypt
from utils.Auth import auth
from utils.pagination import Page
from utils.forms import *
import requests
from bs4 import BeautifulSoup
from django.db.models import F
from django.db import transaction
from utils.response import LikeResponse

def login(request):
    if request.method == "POST":
        response = {'status': True, 'data': None, 'msg': None}
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            user_id = str(UserInfo.objects.get(username=user).id)

            request.session['is_login'] = {'user': user,'user_id':user_id,}
            response['data']={}
        else:
            response['status']=False
            response['msg']=form.errors
        print(response)
        return HttpResponse(json.dumps(response))

def logout(request):
    del request.session['is_login']
    return render(request,'index.html')



def index(request,*args,**kwargs):
    if request.method == "GET":
        register_form = RegisterForm()
        login_form = LoginForm()
        publish_form = PublishForm()
        search_str = request.GET.get("search_string", "")
        current_type_id = kwargs.get('new_type_id')
        if current_type_id: current_type_id = int(current_type_id)
        news_type_list = NewsType.objects.all()
        news_list = News.objects.filter(**kwargs).order_by('-ctime')
        try:
            current_page = int(request.GET.get('page_num'))
        except TypeError:
            current_page = 1
        all_count = news_list.count()
        page_obj = Page(current_page, all_count, request.path_info, search_str)
        news_list = news_list[page_obj.start:page_obj.end]
        page_str = page_obj.page_html()
        user_dict = request.session.get('is_login', None)
        print(user_dict)
        if user_dict:
            username = user_dict['user']

        return render(request, "index.html", locals())



@auth
def add_news(request):
    if request.method =="GET":
        url = request.GET.get('get_url',None)
        print("URL:",url)
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('title').text
            desc = soup.find('meta', attrs={'name': 'description'}).get('content')
            print('Title:',title)
            print('Description:',desc)
            data = {'title': title, 'desc': desc}
        except:
            data = {'title': '没有正确获取到标题', 'desc': '没有正确获取到内容'}
        return HttpResponse(json.dumps(data))
    if request.method == "POST":
        response = {'status':True,'data':None,'msg':None}
        publish_form = PublishForm(request.POST)
        if publish_form.is_valid():

# {'url': 'http://dig.chouti.com/', 'avatar': 'static\\img\\20141120102935_48465.jpg',
#  'summary': '抽屉新..','title': '抽屉..', 'new_type': '1'}
            news_dict = publish_form.cleaned_data

            user_id = request.session.get('is_login',None).get('user_id')

            news_dict.update({'promulgator_id':user_id})
            print(news_dict)
            News.objects.create(**news_dict)

        else:
            response['status'] = False
            response['msg'] = publish_form.errors

        return HttpResponse(json.dumps(response))

@auth
def upload_img(request):
    obj = request.FILES.get('img_data') # 使用FILES接收POST过来的文件
    data = {'status': True,'path': None}
    if obj:
        img_path = os.path.join('static', 'img', obj.name) # 拼接保存路径

        with open(img_path, mode='wb') as f: # 写入路径
            for chunk in obj.chunks():
                f.write(chunk)
        data['path'] = img_path
    else:
        data['status'] = False
    print('ImgPath:',data['path'])
    return HttpResponse(json.dumps(data))

@auth
def digg(request):
    response = LikeResponse()
    try:
        new_id = request.POST.get('new_id')
        uid = 1
        exist_like = models.Like.objects.filter(nnew_id=new_id,uuser_id=uid).count()
        with transaction.atomic():
            if exist_like:
                models.Like.objects.filter(nnew_id=new_id, uuser_id=uid).delete()
                models.News.objects.filter(id=new_id).update(like_count=F('like_count') - 1)
                response.code = 666
            else:
                models.Like.objects.create(nnew_id=new_id,uuser_id=uid)
                models.News.objects.filter(id=new_id).update(like_count=F('like_count') + 1)
                response.code = 999
    except Exception as e:
        response.msg = str(e)
    else:
        response.status = True
    return HttpResponse(json.dumps(response.get_dict()))



    # if request.method == "POST":
    #     response = {'status': True, 'data': None, 'msg': None}
    #     new_id = request.POST.get('new_id')
    #     user_id = request.session.get('is_login', None).get('user_id')
    #     if not Like.objects.filter(news_id=new_id,user_id=user_id):
    #         News.objects.filter(id=new_id).update(like_count=F('like_count')+1)
    #         Like.objects.create(news_id=new_id,user_id=user_id)
    #         response['msg'] = ''
    #     else:
    #         response['msg'] = ''
    #         response['status'] = False
    #     print(response)
    #     return HttpResponse(json.dumps(response))