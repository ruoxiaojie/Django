from django.shortcuts import render,HttpResponse,redirect
from app01.models import *
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    try:
        book_list=Book.objects.all()
        p=Paginator(book_list,10)
        page=request.GET.get("page")
        book_list=p.page(page)
    except PageNotAnInteger:
        book_list = p.page(1)
    except EmptyPage:
        book_list = p.page(p.num_pages)
    return render(request,"index.html",locals())


def class1(request):

    Booklist = []
    for i in range(100):
    Booklist.append(Book(title="book" + str(i), price=30 + i * i))
    Book.objects.bulk_create(Booklist)