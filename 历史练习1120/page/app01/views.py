from django.shortcuts import render,HttpResponse
from app01 import models
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.


def create_temp_data(request):
    for i in range(1,104):
        models.UserInfo.objects.create(username='root%s' %i,
                                       password='123123',
                                       email='root%s@qq.com' %i)
    return HttpResponse("创建成功")

def users1(request):
    current_page=request.GET.get('p')
    user_list = models.UserInfo.objects.all()
    paginator=Paginator(user_list,10)
    try:
        page_obj=paginator.page(current_page)
    except EmptyPage as e:
        page_obj = paginator.page(1)
    except PageNotAnInteger as e:
        page_obj = paginator.page(1)


    return render(request,'users1.html',{'page_obj':page_obj})

'''
    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    # page:     page对象
        # has_next              是否有下一页
        # next_page_number      下一页页码
        # has_previous          是否有上一页
        # previous_page_number  上一页页码
        # object_list           分页之后的数据列表
        # number                当前页
        # paginator             paginator对象
'''

class PageInfo:
    def __init__(self,current_page,pag_num): #当前页  每页条数
        try:
            current_page=int(current_page)
        except Exception as e:
            current_page = int(1)

        self.current_page=current_page
        self.pag_num=pag_num

    def start(self):
        return (self.current_page - 1) * self.pag_num

    def end(self):
        return (self.current_page * self.pag_num)


def users2(request):
    page_info=PageInfo(request.GET.get('p'),10)

    user_list=models.UserInfo.objects.all()[page_info.start():page_info.end()]

    return render(request,'users2.html',{'user_list':user_list})