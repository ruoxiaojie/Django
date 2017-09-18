import requests
from bs4 import BeautifulSoup


response = requests.get('http://music.163.com/#/song?id=188057')
soup = BeautifulSoup(response.text,'html.parser')
title = soup.find('title').text
desc = soup.find('meta',attrs={'name': 'description'}).get('content')
print(title)
print(desc)