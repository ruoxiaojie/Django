from django.shortcuts import render,HttpResponse,redirect
from book_app.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def auth():
    pass

def index(request):
    all_book_list=book.objects.all()
    if request.method == "POST":
        all_book_list=book.objects.filter(title__contains="")
    return render(request,"index.html",{"all_book_list":all_book_list})



def addbook(request):
    if request.method=="POST":
        title=request.POST.get("title")
        price=request.POST.get("price")
        author=request.POST.get("author")
        publish=request.POST.get("publish")
        book.objects.create(title=title,price=price,author=author,publiosh=publish)
        #redirect 跳转
        return redirect("/index/")
    return render(request, "addbook.html")


def delete(request):
    id=request.GET.get("id")
    book.objects.filter(id=id).delete()
    return redirect("/index/")


# 修改 弹窗
#+ def edit(request):
#         id=request.GET.get("id")
#         book.objects.filter(id=id).update()








