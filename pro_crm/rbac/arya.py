#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from arya.service.sites import site
from arya.service.sites import AryaConfig
from . import models

from django.forms import ModelForm
from django.forms import fields
from django.forms import widgets as form_widgets


class RbacPermissionConfig(object):
    pass
    # def get_show_add_btn(self):
    #     code_list = self.request.permission_code_list
    #     if 'add' in code_list:
    #         return True
    #
    # def get_edit_link(self):
    #     code_list = self.request.permission_code_list
    #     if 'edit' in code_list:
    #         return super().get_edit_link()
    #     else:
    #         return []
    #
    # def get_show_list_display(self):
    #     code_list = self.request.permission_code_list
    #     if 'del' in code_list:
    #         return super().get_show_list_display()
    #     else:
    #         list_display = []
    #         if self.list_display:
    #             list_display.extend(self.list_display)
    #             list_display.insert(0, AryaConfig.list_display_checkbox)
    #
    #         return list_display


"""
角色表配置和定制
"""


class RoleModelForm(ModelForm):
    class Meta:
        model = models.Role
        fields = "__all__"
        widgets = {
            'permissions': form_widgets.SelectMultiple(attrs={'style': 'height:200px;'})
        }


class RoleConfig(RbacPermissionConfig, AryaConfig):
    list_display = ['caption', ]
    edit_link = ['caption', ]
    model_form = RoleModelForm


site.register(models.Role, RoleConfig)

"""
用户表配置和定制
"""


class UserConfig(RbacPermissionConfig, AryaConfig):
    list_display = ['username', 'email']
    edit_link = ['username', ]

    def reset_password(self, request):
        """
        定制Action行为
        :param request: 
        :param queryset: 
        :return: False返回当前页面，否则返回执行内容
        """
        code_list = self.request.permission_code_list
        if 'reset_password' not in code_list:
            return None
        pk_list = request.POST.getlist('pk')
        self.model_class.objects.filter(id__in=pk_list).update(password=123)
        # return redirect('/index/')

    reset_password.short_description = "重置密码"

    def get_actions(self):
        actions = []
        code_list = self.request.permission_code_list
        if 'reset_password' in code_list:
            actions.append(UserConfig.reset_password)
        return actions


site.register(models.User, UserConfig)

"""
菜单表配置和定制
"""


class MenuConfig(RbacPermissionConfig, AryaConfig):
    list_display = ['caption', 'parent']
    edit_link = ['caption', ]


site.register(models.Menu, MenuConfig)

"""
权限表配置和定制
"""


def discover_all_url(patterns, prev, first=False, result=[]):
    if first:
        result.clear()
    from django.urls.resolvers import RegexURLPattern
    for item in patterns:
        if isinstance(item, RegexURLPattern):
            val = prev + item._regex.strip('^$')
            result.append((val, val,))
        else:
            discover_all_url(item.urlconf_name, prev + item._regex.strip('^$'))
    return result


class PermissionModelForm(ModelForm):
    url = fields.ChoiceField(required=False)

    class Meta:
        model = models.Permission
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        from pro_crm.urls import urlpatterns
        super(PermissionModelForm, self).__init__(*args, **kwargs)
        # 获取数据库中已存在的数据，基础
        all_url = discover_all_url(urlpatterns, '/', True)

        all_url.insert(0, ['', '请选择URL'])
        db_urls = models.Permission.objects.all().values_list('url', 'url')

        for item in db_urls:
            if item in all_url:
                all_url.remove(item)

        self.fields['url'].choices = all_url


class PermissionConfig(RbacPermissionConfig, AryaConfig):
    list_display = ['caption', 'url', 'group','is_menu']
    edit_link = ['caption', ]

    model_form = PermissionModelForm

    search_list = ['caption', 'url', ]


site.register(models.Permission, PermissionConfig)



