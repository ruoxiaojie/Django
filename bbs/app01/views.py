from django.shortcuts import render,HttpResponse,redirect
from django.db.models import F
from django.db import transaction
from utils.response import LikeReseponse
from app01 import models
import json

def index(request,*args,**kwargs):
    current_new_type_id = kwargs.get('new_type_id')
    if current_new_type_id:
        current_new_type_id = int(current_new_type_id)
    new_type_list = models.NewsType.objects.all()
    new_list = models.News.objects.filter(**kwargs)
    return render(request, 'index.html',
                  {'new_type_list': new_type_list, 'new_list': new_list, 'current_new_type_id': current_new_type_id})



def do_like(request):
    response = LikeReseponse()

    try:
        new_id = request.POST.get('newID')

        uid = 1
        exist_like = models.Like.objects.filter(nnew=new_id,uuser=uid).count()
        with transaction.atomic():
            if exist_like:
                models.Like.objects.filter(nnew=new_id,uuser=uid).delete()
                models.News.objects.filter(id=new_id).update(like_count=F('like_count') - 1)
                response.code = 666
            else:
                models.Like.objects.create(nnew=new_id, uuser=uid)
                models.News.objects.filter(id=new_id).update(like_count=F('like_count') + 1)
                response.code = 999
    except Exception as e:
        response.msg = str(e)
    else:
        response.status = True
    return HttpResponse(json.dumps(response.get_dict()))






