from django.shortcuts import render,HttpResponse
from app01 import models
import os
def index(request,*args,**kwargs):
    """
    首页：
        - 显示所有的新闻类型
        - 显示所有新闻列表
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    # None, "1"  "2"
    current_new_type_id = kwargs.get('new_type_id')
    if current_new_type_id:
        current_new_type_id = int(current_new_type_id)
    new_type_list = models.NewsType.objects.all()

    new_list = models.News.objects.filter(**kwargs)

    return render(request,'index.html',{'new_type_list':new_type_list,'new_list':new_list,'current_new_type_id':current_new_type_id})


def upload(request):
    return render(request,'upload.html')

def upload_img(request):
    obj = request.FILES.get('a1')

    img_path = os.path.join('static','img',obj.name)

    with open(img_path,mode='wb') as f:
        for chunk in obj.chunks():
            f.write(chunk)
    data = {
        'status': True,
        'path': img_path
    }
    import json
    return HttpResponse(json.dumps(data))

