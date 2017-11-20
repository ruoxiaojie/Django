#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-

class Page(object):
    def __init__(self,current_page,all_count,base_url,search_str=None,per_page=7,pager_page_count=9):
        self.base_url = base_url
        self.search_str = search_str
        self.current_page = current_page
        self.per_page = per_page
        self.all_count = all_count
        self.pager_page_count = pager_page_count
        pager_count, b = divmod(all_count, per_page)
        if b != 0:
            pager_count += 1
        self.pager_count = pager_count

        half_pager_page_count = int(pager_page_count / 2)
        self.half_pager_page_count = half_pager_page_count

    @property
    def start(self):
        return (self.current_page - 1) * self.per_page

    @property
    def end(self):
        return self.current_page * self.per_page

    def page_html(self):
        if self.pager_count < self.pager_page_count:
            pager_start = 1
            pager_end = self.pager_count
        else:
            if self.current_page <= self.half_pager_page_count:
                pager_start = 1
                pager_end = self.pager_page_count
            else:
                if (self.current_page + self.half_pager_page_count) > self.pager_count:
                    pager_end = self.pager_count
                    pager_start = self.pager_count - self.pager_page_count + 1
                else:
                    pager_start = self.current_page - self.half_pager_page_count
                    pager_end = self.current_page + self.half_pager_page_count

        page_list = []
        first_page='<li><a href="%s?search_string=%s">首页</a></li>'%(self.base_url,self.search_str)
        page_list.append(first_page)
        if self.current_page <= 1:
            prev = '<li><a href="#">&laquo;</a></li>'
        else:
            prev = '<li><a href="%s?page_num=%s&search_string=%s">&laquo;</a></li>' % (self.base_url,self.current_page - 1,self.search_str)
        page_list.append(prev)
        for i in range(pager_start, pager_end + 1):
            if self.current_page == i:
                tpl = '<li><span class="ct_pagepw">%s</span></li>' %i
            else:
                tpl = '<li><a href="%s?page_num=%s&search_string=%s">%s</a></li>' % (self.base_url,i,self.search_str, i,)
            page_list.append(tpl)

        if self.current_page >= self.pager_count:
            nex = '<li><a href="#">&raquo;</a></li>'
        else:
            nex = '<li><a href="%s?page_num=%s&search_string=%s">&raquo;</a></li>' % (self.base_url,self.current_page + 1,self.search_str)
        page_list.append(nex)
        trailer_page = '<li><a href="%s?page_num=%s&search_string=%s">尾页</a></li>' % (self.base_url,self.pager_count,self.search_str)
        page_list.append(trailer_page)
        page_str = "".join(page_list)
        return page_str