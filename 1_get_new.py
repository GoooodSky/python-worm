# coding:utf-8
import urllib2
from bs4 import BeautifulSoup

# 获取最新的杂志
response = urllib2.urlopen('http://www.pdfzj.com/tag/微型计算机')
html = response.read()
soup = BeautifulSoup(html, "html.parser")
content = soup.article.find("a").get('href')
title = soup.article.img.get('alt')
time = soup.article.time.get_text()

print "更新到：",time , title, content



