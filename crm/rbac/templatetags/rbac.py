#!/usr/bin/python3.5

from django.template import Library
from django.conf import settings
import re
register = Library()

@register.inclusion_tag('menu_tpl.html')
def menu_html(request):
    page_menu = {}
    current_url = request.path_info
    # current_url = "/userinfo/"

    permission_menu_list = request.session[settings.OO]
    for item in permission_menu_list:
        url = item['url']
        regex = settings.URL_FORMAT.format(url)
        if re.match(regex, current_url):
            item['opened'] = True

        menu_id = item['menu_id']
        opened = "active" if item.get('opened') else ""

        child = {'title': item['title'], 'url': item['url'], 'opened': opened}
        if menu_id in page_menu:
            page_menu[menu_id]['children'].append(child)
            if opened:
                page_menu[menu_id]['opened'] = opened
        else:
            page_menu[menu_id] = {'opened': opened, 'menu_title': item['menu_title'], 'children': [child, ]}
    return {'page_menu':page_menu}