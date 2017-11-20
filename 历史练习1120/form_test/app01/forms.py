#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-

from django.forms import Form,fields,widgets
from app01 import models

class UserInfoForm(Form):
    name = fields.CharField(
        required=True,
        min_length=6,
        max_length=32)
    email = fields.EmailField(
        required=True,
        min_length=6,
        max_length=64
    )
    phone = fields.CharField(validators=[])
    dp_id = fields.ChoiceField(
        choices=[]
    )

    def __init__(self,*args,**kwargs):
        super(UserInfoForm,self).__init__(*args,**kwargs)
        self.fields['dp_id'].choices = models.Depart.objects.values_list('id','title')

    def clean_phone(self):
        """
        切勿瞎取值
        :return: 必须有返回值，
        """
        # 去取用户提交的值：可能是错误的，可能是正确
        value = self.cleaned_data['phone']

        return value