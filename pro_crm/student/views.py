from django.shortcuts import render, redirect, HttpResponse
from django.forms import Form
from django.forms import fields
from django.forms import widgets

from crm import models


def auth(func):
    def inner(request, *args, **kwargs):
        student_info = request.session.get('student_info')
        if not student_info:
            return redirect('/student/login/')
        return func(request, *args, **kwargs)

    return inner


def login(request):
    """
    学生登录
    :param request: 
    :return: 
    """
    if request.method == 'GET':
        return render(request, 'student/login.html')
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    obj = models.Student.objects.filter(username=user, password=pwd).first()
    if obj:
        request.session["student_info"] = {'nid': obj.id, 'name': obj.username}
        return redirect('/student/index/')
    return render(request, 'student/login.html')


@auth
def index(request):
    """
    学生首页
    :param request: 
    :return: 
    """
    student_id = request.session['student_info']['nid']
    student_obj = models.Student.objects.filter(pk=student_id).first()
    class_list = student_obj.class_list.all()

    survery_list = models.Survery.objects.filter(by_class__in=class_list)

    return render(request, 'student/index.html',{"survery_list":survery_list})


@auth
def evaluate(request, cls_id, survery_id):
    """
    学生进行问卷调查
    :param request: 
    :param cls_id: 班级ID
    :param survery_id: 问卷ID
    :return: 
    """
    student_id = request.session['student_info']['nid']
    is_class_student = models.Student.objects.filter(id=student_id, class_list__in=[cls_id, ]).count()
    if not is_class_student:
        return HttpResponse('不是本班学生无权评价')

    is_evaluated = models.SurveryRecord.objects.filter(student_name_id=student_id, survery_id=survery_id).count()
    if is_evaluated:
        return HttpResponse('你已经评价过，无法再次进行')

    survery_obj = models.Survery.objects.filter(pk=survery_id).first()
    if not survery_obj:
        return HttpResponse('问卷不存在')

    survery_item_list = models.SurveryItem.objects.filter(survery_id=survery_id)

    # 动态创建Django Form组件，用于生成页面中的问卷选项和错误信息提示
    field_dict = {}
    for i in range(len(survery_item_list)):
        item = survery_item_list[i]
        print(item.answer_type, item.name)
        if item.answer_type == 1:
            # 分值
            field_dict["score_{0}".format(item.pk)] = fields.ChoiceField(label=item.name,
                                                                         choices=[(i, i) for i in range(1, 11)],
                                                                         widget=widgets.RadioSelect)
        elif item.answer_type == 2:
            # 选择

            field_dict["single_id_{0}".format(item.pk)] = fields.ChoiceField(label=item.name,
                                                                             choices=models.SurveryChoices.objects.filter(
                                                                                 item_id=item.pk).values_list('pk',
                                                                                                              'content'),
                                                                             widget=widgets.RadioSelect)
        elif item.answer_type == 3:
            # 建议
            field_dict["suggestion_{0}".format(item.pk)] = fields.CharField(label=item.name,
                                                                            widget=widgets.Textarea)
        else:
            pass
    EvaluateForm = type("EvaluateForm", (Form,), field_dict)

    if request.method == 'GET':
        # 学生查看问卷问题
        form = EvaluateForm()
        return render(request, 'student/evaluate.html', {'form': form})
    else:
        # 学生提交问卷
        form = EvaluateForm(request.POST)
        if form.is_valid():
            survery_record_list = []
            for k, v in form.cleaned_data.items():
                field_name, item_id = k.rsplit('_', 1)
                obj = models.SurveryRecord(**{"survery_id": survery_id, "student_name_id": student_id, field_name: v,
                                              'survery_item_id': item_id})
                survery_record_list.append(obj)
            print(survery_item_list)
            models.SurveryRecord.objects.bulk_create(survery_record_list)
            return HttpResponse('感谢您的参与！！！')
        return render(request, 'student/evaluate.html', {'form': form})
