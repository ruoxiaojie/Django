#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-

from django.conf import settings
def init_permission(request,user):
    #用户权限信息初始化，获取当前用户所有权限信息，并保存到Session中
    permission_list = user.roles.filter(permissions__id__isnull=False).values(
        'permissions__id',
        'permissions__title',
        'permissions__url',
        'permissions__code',
        'permissions__group',
        'permissions__is_menu'
    ).distinct()
    #print(permission_list)
    """
    {
        1:{'codes':['list','add'],urls:['/userinfo/','/userinfo/add/']},
        2:{'codes':['list','add'],urls:['/order/','/order/add/']},
    }
    """
    permission_dict = {}
    for item in permission_list:
        group_id = item['permissions__group']
        code = item['permissions__code']
        url = item['permissions__url']
        if group_id in permission_dict:
            permission_dict[group_id]['codes'].append(code)
            permission_dict[group_id]['urls'].append(url)
        else:
            permission_dict[group_id] = {"codes": [code, ], "urls": [url, ]}

    request.session[settings.XX] = permission_dict