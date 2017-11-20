from django.shortcuts import render,HttpResponse,redirect
from Mybook.models import Book
from django.views.decorators.csrf import csrf_protect



def index(request):
    if request.method == 'GET':
        book_list = Book.objects.all()
        return  render(request,'base.html',{"book_list":book_list})
    elif request.method == 'POST':
        if request.POST.get('search_title',None):
            book_list = Book.objects.filter(title__icontains=request.POST.get('search_title'))
        else:
            book_list = Book.objects.all()
        return render(request, 'base.html', {"book_list": book_list})


@csrf_protect
def add(request):
    if request.method == 'POST':
        msg_dic = request.POST
        Book.objects.create(title=msg_dic.get('title_name'),author=msg_dic.get('author_name'),price=msg_dic.get('price_num'),publish=msg_dic.get('publish_name')
                            ,date=msg_dic.get('time_num'),describe=msg_dic.get('desc'))

        return redirect('/index/')

    return render(request,'add.html')


def delete(request):
    if request.method == 'GET':
        msg_dic = request.GET
        Book.objects.filter(id=msg_dic.get('id')).delete()
        return redirect('/index/')


def show(request):
    if request.method == 'GET':
        msg_dic = request.GET
        book_desc = Book.objects.filter(id=msg_dic.get('id'))
        #book_desc = Book.objects.filter(id=msg_dic.get('id')).first()
        return render(request,'desc.html',{"book_desc":book_desc})

def modify(request):
    new_dic = {}
    msg_dic = request.POST
    for k,v in dict(msg_dic).items():
        if k == 'csrfmiddlewaretoken' or k == 'id':
            continue
        else:
            new_dic[k] = v[0]
    Book.objects.filter(id=msg_dic.get('id')).update(**new_dic)
    return  redirect('/index/')




