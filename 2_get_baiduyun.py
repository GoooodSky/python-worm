# coding:utf-8
import urllib2
import re
from bs4 import BeautifulSoup

# 获取百度云链接和密码
def get_baiduyun_url_psw(url):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    content = soup.get_text()
    baiduyun_url = re.search(u'(?<=\u94fe\u63a5\uff1a).+(?=\u5bc6\u7801)', content).group(0)
    baiduyun_psw = re.search(u'(?<=\u5bc6\u7801\uff1a).+', content).group(0)
    return baiduyun_url, baiduyun_psw

http, psw = get_baiduyun_url_psw('http://www.pdfzj.com/13224.html')

print http, psw

