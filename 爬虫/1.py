#!/usr/bin/python3.5
# Author: xiaojie
import requests
from bs4 import BeautifulSoup
#
# url = requests.get('http://blog.sina.com.cn/s/blog_a25d27670102x91x.html?tj=hist')
# url.encoding='utf-8'
#
# res=BeautifulSoup(url.text,'html.parser')
# title = res.select('title')[0].text
# print(title)

url = requests.get('http://roll.news.sina.com.cn/news/gnxw/gdxw1/index.shtml')
url.encoding='gbk'
res=BeautifulSoup(url.text,'html.parser')
li_obj=res.find(name='div',attrs={'class':'listBlk'})
li_obj_list = li_obj.find_all('li')
for title in li_obj_list:
	r = title.find(name='a')
	print(r.text)
# print(res)
