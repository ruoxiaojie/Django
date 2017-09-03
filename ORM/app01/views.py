from django.shortcuts import render,HttpResponse
from app01.models import *
# Create your views here.

def index(request):
    return HttpResponse("okokok")

def add(request):
    # Book.objects.create(title="python",price=188) #一对一添加

    # Book_obj=Book(title="python",price=188)
    #Book_obj.save()
    # #一对一添加


    #一对多
    # Book.objects.create(title="python",price=188,publisher_id=2) #添加方式1
#一对多添加方式2
    # Book_obj=Book.objects.get(nid=1)
    # print(Book_obj.title)
    # print(Book_obj.price)
    # print(Book_obj.publisher) #publish object  需要在publish表添加__str__方法


#多对多的添加方式
    book_obj=Book.objects.get(nid=2)
    # auth_list=Author.objects.all()
    # book_obj.aushor.add(*auth_list) #nid=2的书籍作者的对象集合

    book_obj.aushor.clear() #和id=2的书都删除
    return HttpResponse("ok")
'''
  #  一对多的添加方式二
    publish_obj=publish.objects.get(id=1)
    book_obj=Book(title="linux",price=100)
    book_obj.publisher=publish_obj
    book_obj.save()   
'''



def query(request):
    # ret=Book.objects.values("title","price")
    ret=Book.objects.filter(nid__gt=2).values("title","price")
    

    print(ret)
    return HttpResponse("ok")






