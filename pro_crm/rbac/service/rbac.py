#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from django.conf import settings
from .. import models


def initial_permission(request, user):
    """
    初始化权限，获取当前用户权限并添加到session中
    
    :param request: 请求对象
    :param user: 当前用户对象
    :return: 
    """

    # 1.获取角色对应的所有权限
    permission_list = user.roles.values(
        'permissions__id',
        'permissions__caption',
        'permissions__url',
        'permissions__code',
        'permissions__is_menu',
        'permissions__group_id',
        'permissions__group__is_group',
        'permissions__group__parent_id'
    ).distinct()

    for item in permission_list:
        print(item)

    permission_url_dict = {}
    permission_menu_list = []

    for item in permission_list:
        group_id = item['permissions__group_id']
        url = item['permissions__url']
        code = item['permissions__code']
        url_list = [url, ] if url else []
        if group_id in permission_url_dict:
            permission_url_dict[group_id]['codes'].append(code)
            permission_url_dict[group_id]['urls'].extend(url_list)
        else:
            permission_url_dict[group_id] = {'codes': [code, ], 'urls': url_list}

        if item['permissions__is_menu']:
            tpl = {
                'permissions__id': item['permissions__id'],
                'permissions__caption': item['permissions__caption'],
                'permissions__url': item['permissions__url'],
                'permissions__menu_id': item['permissions__group__parent_id']
            }
            permission_menu_list.append(tpl)

    # 2. 权限写入session
    request.session[settings.RBAC_PERMISSION_URL_SESSION_KEY] = permission_url_dict

    # 3. 菜单写入session
    menu_list = list(models.Menu.objects.filter(is_group=False).values('id', 'caption', 'parent_id'))
    request.session[settings.RBAC_MENU_PERMISSION_SESSION_KEY] = {
        settings.RBAC_MENU_KEY: menu_list,
        settings.RBAC_MENU_PERMISSION_KEY: permission_menu_list
    }
