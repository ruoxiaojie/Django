from django.forms import Form
from django.forms import fields
from django.forms import widgets
from app01 import models
import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class UserInfoForm(Form):
    name = fields.CharField(
        required=True,
        min_length=6,
        max_length=12
    )    # 用户提交数据是字符串
    email = fields.EmailField()  # 用户提交数据是字符串，邮箱正则

    # 方式一：RegexValidator对象

    # 方式二：函数


    # 方法三：当前类的方法中，方法名称要求: clean_phone方法
    # phone = fields.CharField()

    dp_id = fields.ChoiceField(
        choices=[]
    )
    def __init__(self,*args,**kwargs):
        # 找到类中的所有静态字段拷贝并且赋值给self.fields
        super(UserInfoForm,self).__init__(*args,**kwargs)
        self.fields['dp_id'].choices = models.Depart.objects.values_list('id', 'title')

    def clean_phone(self):
        """
        切勿瞎取值
        :return: 必须有返回值，
        """
        # 去取用户提交的值：可能是错误的，可能是正确
        value = self.cleaned_data['phone']


        return value