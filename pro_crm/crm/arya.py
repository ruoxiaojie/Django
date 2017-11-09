#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json

from django.shortcuts import HttpResponse, render, redirect
from django.urls import reverse
from django.forms import modelformset_factory

from django.utils.safestring import mark_safe
from django.db.models import Q
from django.forms import ModelForm
from django.forms import widgets as form_widgets
from django.db import transaction

from . import models
from arya.service.sites import site
from arya.service.sites import AryaConfig
from arya.service.sites import FilterOption

site.register(models.School)
site.register(models.Course)
site.register(models.Department)
site.register(models.UserInfo)


class ClassListConfig(AryaConfig):
    def course_display(self, obj=None, is_header=False):
        if is_header:
            return "课程"
        return "{0}({1}期)".format(obj.course.name, obj.semester)

    def numbers_display(self, obj=None, is_header=False):
        if is_header:
            return "人数"

        student_count = obj.student_set.all().count()
        return student_count

    list_display = [course_display, numbers_display]


site.register(models.ClassList, ClassListConfig)


class CustomerConfig(AryaConfig):
    def source_display(self, obj=None, is_header=False):
        if is_header:
            return '来源'
        else:
            return obj.get_source_display()

    def gender_display(self, obj=None, is_header=False):
        if is_header:
            return '性别'
        else:
            return obj.get_gender_display()

    def education_display(self, obj=None, is_header=False):
        if is_header:
            return '学历'
        else:
            return obj.get_education_display()

    def tracking_display(self, obj=None, is_header=False):
        if is_header:
            return "跟进记录"

        count = obj.consultrecord_set.all().count()
        tpl = "<a href='/arya/crm/consultrecord/?customer={0}'>跟进记录({1})</a>".format(obj.pk, count, )

        return mark_safe(tpl)

    def status_display(self, obj=None, is_header=False):
        if is_header:
            return '状态'
        else:
            return obj.get_status_display()

    list_display = ['qq', 'name', education_display, gender_display, source_display, tracking_display, status_display]

    edit_link = ['qq', ]

    list_filter = [
        FilterOption('gender'),
        FilterOption('status'),
        FilterOption('source', is_multi=True),
        FilterOption('consultant', False, None, lambda x: x.name, lambda x: x.pk),
    ]
    search_list = ['qq', 'name']


site.register(models.Customer, CustomerConfig)


class ConsultRecordConfig(AryaConfig):
    list_display = ['customer', 'consultant', 'date', 'note']


site.register(models.ConsultRecord, ConsultRecordConfig)


class StudentConfig(AryaConfig):
    list_display = ['username', ]


site.register(models.Student, StudentConfig)


class PaymentRecordConfig(AryaConfig):
    list_display = ['customer', 'class_list', 'consultant']


site.register(models.PaymentRecord, PaymentRecordConfig)


class CourseRecordConfig(AryaConfig):
    """
    老师上课记录
    """

    def student_num_display(self, obj=None, is_header=False):
        if is_header:
            return '学生人数'

        count = models.StudyRecord.objects.filter(course_record=obj).count()
        return count

    list_display = ['class_obj', 'day_num', 'teacher', 'course_title', student_num_display]
    edit_link = ['class_obj']

    def init_study_record(self, request):
        """
        初始化上课记录
        :return: 
        """
        pk_list = request.POST.getlist('pk')
        course_record_list = self.model_class.objects.filter(pk__in=pk_list)
        for row in course_record_list:
            students = models.Student.objects.filter(class_list=row.class_obj)
            for student in students:
                models.StudyRecord.objects.get_or_create(**{'course_record': row, 'student': student})

    init_study_record.short_description = "初始化上课记录"

    actions = [init_study_record, ]


site.register(models.CourseRecord, CourseRecordConfig)


class StudyRecordConfig(AryaConfig):
    """
    学生学习记录
    """
    list_display = ['course_record', 'student']


site.register(models.StudyRecord, StudyRecordConfig)


# ################ 调查问卷 ################
class SurveryItemModelForm(ModelForm):
    class Meta:
        model = models.SurveryItem
        exclude = ['id', 'survery']
        widgets = {
            'name': form_widgets.Textarea(attrs={'class': 'form-control'}),
            'answer_type': form_widgets.Select(attrs={'class': 'form-control answer-type'}),
        }


class SurveryChoicesModelForm(ModelForm):
    class Meta:
        model = models.SurveryChoices
        exclude = ['id', 'item']


class SurveryConfig(AryaConfig):
    def survery_item_display(self, obj=None, is_header=False):
        if is_header:
            return '问卷选项'
        params = self.back_url_param()
        if params:
            tpl = "<a href='{0}?{1}'>编辑问卷</a>".format(
                self.items_url(obj.pk),
                self.back_url_param())
        else:
            tpl = "<a href='{0}'>编辑问卷</a>".format(
                self.items_url(obj.pk))
        return mark_safe(tpl)

    def show_score_display(self, obj=None, is_header=False):
        if is_header:
            return '查看评分'

        params = self.back_url_param()
        if params:
            tpl = "<a href='{0}?{1}'>查看评分</a>".format(
                self.calculate_url(obj.pk),
                self.back_url_param())
        else:
            tpl = "<a href='{0}'>查看评分</a>".format(
                self.calculate_url(obj.pk))
        return mark_safe(tpl)


    def student_num_display(self, obj=None, is_header=False):
        if is_header:
            return '参与人数'
        from django.db.models import Count
        # 班级总人数
        all_count = models.Student.objects.filter(class_list=obj.by_class).count()
        # 参与评分人数
        count = models.SurveryRecord.objects.filter(survery=obj).values('student_name_id').annotate(ct=Count('student_name_id')).count()
        return '{0}/{1}'.format(count,all_count)

    def evaluate_display(self, obj=None, is_header=False):
        if is_header:
            return '调查地址'
        url = "<a href='/student/evaluate/{0}/{1}/'>/student/evaluate/{0}/{1}/</a>".format(obj.by_class_id, obj.pk)
        return mark_safe(url)

    list_display = ['name', 'by_class', student_num_display, survery_item_display, evaluate_display, show_score_display]
    edit_link = ['name']

    def extra_urls(self):
        from django.conf.urls import url
        app_model_name = (self.app_label, self.model_name,)
        urls = [
            url(r'^(.+)/items/$', self.wrapper(self.survery_items), name="%s_%s_items" % app_model_name),
            url(r'^(.+)/calculate/$', self.wrapper(self.survery_calculate), name="%s_%s_calculate" % app_model_name),
        ]
        return urls

    def items_url(self, pk):
        base_url = reverse("{0}:{1}_{2}_items".format(self.site.namespace, self.app_label, self.model_name), args=(pk,))
        return base_url

    def calculate_url(self, pk):
        base_url = reverse("{0}:{1}_{2}_calculate".format(self.site.namespace, self.app_label, self.model_name), args=(pk,))
        return base_url

    def survery_items(self, request, survery_id):

        if request.method == 'GET':
            obj = models.Survery.objects.filter(pk=survery_id).first()
            if not obj:
                return redirect(self.changelist_url_params)

            def inner():
                survery_item_list = models.SurveryItem.objects.filter(survery_id=survery_id)
                for item in survery_item_list:
                    row = {'item': item, 'form': SurveryItemModelForm(instance=item), 'choices': None,
                           'option_class': 'hide'}
                    if item.answer_type == 2:
                        def inner_loop(obj):
                            choices = models.SurveryChoices.objects.filter(item=obj).all()
                            for v in choices:
                                yield {"form": SurveryChoicesModelForm(instance=v), 'obj': v}

                        row['option_class'] = ""
                        row['choices'] = inner_loop(item)
                    yield row
                if not survery_item_list:
                    yield {'item': None, 'form': SurveryItemModelForm(), 'choices': None, 'option_class': 'hide'}

            return render(request, 'crm/survery_items.html', {'survery_item_list': inner()})
        else:
            response = {'status': 999, 'data': None, 'msg': None}
            try:
                survery_obj = models.Survery.objects.filter(pk=survery_id).first()
                if not survery_obj:
                    response['status'] = 1001
                    response['msg'] = "请选择调查问卷，再创建问题！"
                    return HttpResponse(json.dumps(response))

                post_list = json.loads(request.body.decode('utf-8'))
                if not post_list:
                    response['status'] = 1002
                    response['msg'] = "未创建调查问卷问题"
                    return HttpResponse(json.dumps(response))

                # 获取用户提交的问卷问题和数据库已经有的问卷问题
                post_pk_list = [row.get('pk') for row in post_list if row.get('pk')]
                survery_item_list = survery_obj.surveryitem_set.all()
                survery_item_dict = {str(v.pk): v for v in survery_item_list}
                del_item_ids = set(survery_item_dict.keys()).difference(post_pk_list)

                error_count = 0
                error_list = {}
                # 创建当前问卷的新问题和更新原来的问题
                for i in range(len(post_list)):
                    try:
                        item = post_list[i]
                        with transaction.atomic():
                            pk = item.get('pk')
                            name = item.get('name')
                            answer_type = item.get('answer_type')
                            options = item.get('options')

                            # 创建新的问题
                            if pk not in survery_item_dict:
                                item_obj = models.SurveryItem.objects.create(name=name, answer_type=answer_type,
                                                                             survery=survery_obj)
                                if answer_type == '2':
                                    # 如果是单选题，则创建选项
                                    for option in options:
                                        try:
                                            option['points'] = int(option['points'])
                                        except Exception as e:
                                            option['points'] = 0
                                        models.SurveryChoices.objects.create(item=item_obj, content=op['content'],
                                                                             points=op['points'])
                            # 更新已有的问题
                            else:

                                item_obj = survery_item_dict[pk]
                                item_obj.name = name
                                item_obj.answer_type = answer_type
                                item_obj.save()
                                if answer_type == '2':
                                    # 如果是单选题
                                    choice_list = item_obj.surverychoices_set.all()
                                    choice_dict = {str(v.pk): v for v in choice_list}
                                    for op in options:
                                        op_pk = op.get('pk')
                                        op_content = op.get('content')
                                        try:
                                            op_points = int(op.get('points'))
                                        except Exception as e:
                                            op_points = 0
                                        # 创建新选项
                                        if op_pk not in choice_dict:
                                            models.SurveryChoices.objects.create(item=item_obj, content=op_content,
                                                                                 points=op_points)
                                        # 更新原选项
                                        else:
                                            op_obj = choice_dict[op_pk]
                                            op_obj.content = op_content
                                            op_obj.points = op_points
                                            op_obj.save()
                                    # 删除已经不存在的选项
                                    option_pk_list = [m.get('pk') for m in options if m.get('pk')]
                                    del_choice_ids = set(choice_dict.keys()).difference(option_pk_list)
                                    models.SurveryChoices.objects.filter(id__in=del_choice_ids).delete()

                                else:
                                    models.SurveryChoices.objects.filter(item=item_obj).delete()

                    except Exception as e:
                        error_list[i] = str(e)
                        error_count += 1
                if error_count:
                    response['status'] = 1003
                    response['msg'] = error_list
                    response['data'] = "部分失败（{0}/{1}）".format(error_count, len(post_list))
                else:
                    response['data'] = "执行成功（{0}/{1}）".format(len(post_list), len(post_list))

                # 删除已不存在问题
                models.SurveryItem.objects.filter(id__in=del_item_ids).delete()
            except Exception as e:
                response['status'] = 1000
                response['msg'] = str(e)

            return HttpResponse(json.dumps(response))


    def survery_calculate(self,request, survery_id):
        """
        计算，统计问卷
        :param request: 
        :param survery_id: 
        :return: 
        """
        print(survery_id)
        survery = models.Survery.objects.filter(pk=survery_id).first()
        if not survery:
            return HttpResponse('问卷不存在')
        survery_record = models.SurveryRecord.objects.filter(survery=survery).order_by('student_name_id')

        return render(request,'crm/survery_calculate.html',{"survery_record":survery_record})




site.register(models.Survery, SurveryConfig)











