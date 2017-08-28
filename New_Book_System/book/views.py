from django.shortcuts import render,redirect,HttpResponse
from book import models
from django.forms import Form,ModelForm
from django.views import View
from utils.page import PageInfo

# Create your views here.
# def login(req):
#     if req.method == 'POST':
#         username = req.POST.get('username')
#         password = req.POST.get('password')
#         if username == 'zhangmingyang' and password == '123':
#             #如果登陆成功,则直接跳转到后续页面
#             return redirect('/back/')
#     #如果登陆不成功,仍然停留在当前页面
#     else:
#         return render(req,'index.html')


"""
不使用上面的方式,用一个新的方法试一试
"""
class LogUser(View):
    #为什么form表单走的是第二个get方法,经过检查,走的是post方法==>没错
    def post(self,request):
        print('post.....')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'zhangmingyang' and password == '123':
            # 如果登陆成功,则直接跳转到后续页面
            return redirect('/back/')
        else:
            return render(request, 'index.html')
    def get(self,request):
        print('post.....')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'zhangmingyang' and password == '123':
            # 如果登陆成功,则直接跳转到后续页面
            return redirect('/back/')
        else:
            return render(request, 'index.html')


def back(req):
    #接下来开始编写后台页面
    all_count = models.Book.objects.all().count()
    page_info = PageInfo(req.GET.get('p'), 5, all_count, req.path_info)
    all_book_list = models.Book.objects.all()[page_info.start():page_info.end()]
    return render(req, 'backend.html', {'all_book_list': all_book_list, 'page_info': page_info})



def addBook(req):
    if req.method == 'POST':
        id = req.POST.get("bookID")
        title = req.POST.get("title")
        author = req.POST.get("author")
        publish = req.POST.get("publish")
        price = req.POST.get("price")
        category = req.POST.get("category")
        for publisher in models.Publisher.objects.all():
             if publisher.name.strip() == str(category):
                p_id = publisher.id
                break
        models.Book.objects.create(title=title, author=author,
                                   publication_date = publish,price=price,
                                   pub_id=p_id)
        return redirect("/back/")
    return render(req,"addBook.html")

def delBook(req):
    #先从页面http://127.0.0.1:8000/delete/?id=8011获取id对应的数值
    id = req.GET.get('id')
    models.Book.objects.filter(id=id).delete()
    return redirect("/back/")


def editBook(req):
    if req.method == 'POST':
        id = req.POST.get("bookID")
        title = req.POST.get("title")
        author = req.POST.get("author")
        publish = req.POST.get("publish")
        price = req.POST.get("price")
        category = req.POST.get("category")
        for publisher in models.Publisher.objects.all():
             if publisher.name.strip() == str(category):
                p_id = publisher.id
                break
        models.Book.objects.filter(id=id).update(title=title, author=author,
                                   publication_date = publish,price=price,
                                   pub_id=p_id)
        return redirect("/back/")


def searchBook(req,category):
    obj = models.Book.objects.filter(title__contains=category)
    return render(req, "backend.html", {'all_book_list': obj})