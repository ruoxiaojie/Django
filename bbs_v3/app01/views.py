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