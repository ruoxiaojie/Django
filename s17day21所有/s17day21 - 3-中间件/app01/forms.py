from django.forms import Form
from django.forms import fields
from django.forms import widgets
from app01 import models
import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

"""
def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')

class UserInfoForm(Form):
    name = fields.CharField(
        required=True,
        min_length=6,
        max_length=12
    )    # 用户提交数据是字符串
    email = fields.EmailField()  # 用户提交数据是字符串，邮箱正则

    # 方式一：RegexValidator对象
    # phone = fields.CharField(
    #     validators=[RegexValidator(r'^[0-9]+$', '请输入数字'), RegexValidator(r'^159[0-9]+$', '数字必须以159开头')])   # ？自定义验证规则进行验证

    # 方式二：函数
    # phone = fields.CharField(
    #         validators=[mobile_validate,])   # ？自定义验证规则进行验证

    # 方法三：当前类的方法中，方法名称要求: clean_phone方法
    phone = fields.CharField()

    dp_id = fields.ChoiceField(
        choices=[]
    )
    def __init__(self,*args,**kwargs):
        # 找到类中的所有静态字段拷贝并且赋值给self.fields
        super(UserInfoForm,self).__init__(*args,**kwargs)
        self.fields['dp_id'].choices = models.Depart.objects.values_list('id', 'title')

    def clean_phone(self):
        # 去取用户提交的值：可能是错误的，可能是正确
        value = self.cleaned_data['phone']
        mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
        if not mobile_re.match(value):
            raise ValidationError('手机号码格式错误')

        if models.UserInfo.objects.filter(phone=value).count():
            raise ValidationError('手机号码已经存在')

        return value

"""

"""
class UserInfoForm(Form):
    name = fields.CharField()
    email = fields.EmailField()
    phone = fields.CharField(validators=[RegexValidator(r'^[0-9]+$', '请输入数字')])
    def clean_phone(self):
        # 去取用户提交的值：可能是错误的，可能是正确
        value = self.cleaned_data['phone']
        mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
        if not mobile_re.match(value):
            raise ValidationError('手机号码格式错误')

        if models.UserInfo.objects.filter(phone=value).count():
            raise ValidationError('手机号码已经存在')

        return value

# form = UserInfoForm(request.POST)
# if form.is_valid():
# 内部循环，name，CharField，request.POST.get("name")
# 内部循环，email，CharField，request.POST.get("email")
# 内部循环，phone，CharField，request.POST.get("phone")
"""


class RegisterForm(Form):
    name = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'c1'})
    )
    email = fields.EmailField(
        widget=widgets.EmailInput(attrs={'class':'c1'})
    )
    phone = fields.CharField(
        widget=widgets.Textarea(attrs={'class':'c1'})
    )
    pwd = fields.CharField(
        widget=widgets.PasswordInput(attrs={'class':'c1'})
    )
    pwd_confirm = fields.CharField(
        widget=widgets.PasswordInput(attrs={'class': 'c1'})
    )
    # 单选：select
    # city = fields.ChoiceField(
    #     choices=[(0,"上海"),(1,'北京')],
    #     widget=widgets.Select(attrs={'class': 'c1'})
    # )
    # 多选：select
    # city = fields.MultipleChoiceField(
    #     choices=[(1,"上海"),(2,'北京')],
    #     widget=widgets.SelectMultiple(attrs={'class': 'c1'})
    # )

    # 单选：checkbox
    # city = fields.CharField(
    #     widget=widgets.CheckboxInput()
    # )

    # 多选：checkbox
    # city = fields.MultipleChoiceField(
    #     choices=((1, '上海'), (2, '北京'),),
    #     widget=widgets.CheckboxSelectMultiple
    # )

    # 单选：radio
    # city = fields.CharField(
    #     initial=2,
    #     widget=widgets.RadioSelect(choices=((1,'上海'),(2,'北京'),))
    # )



    def clean(self):
        pwd = self.cleaned_data['pwd']
        pwd_confirm = self.cleaned_data['pwd_confirm']
        if pwd == pwd_confirm:
            return self.cleaned_data
        else:
            from django.core.exceptions import ValidationError
            # self.add_error('pwd', ValidationError('密码输入不一致'))
            self.add_error('pwd_confirm', ValidationError('密码输入不一致'))
            return self.cleaned_data








