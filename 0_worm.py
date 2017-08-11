# coding:utf-8
import re
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 获取最新的杂志
def get_new(url):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    herf = soup.article.find("a").get('href')
    title = soup.article.img.get('alt')
    time = soup.article.time.get_text()
    return time, title, herf

# 获取百度云链接和密码
def get_baiduyun_url_psw(url):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    content = soup.get_text()
    baiduyun_url = re.search(u'(?<=\u94fe\u63a5\uff1a).+(?=\u5bc6\u7801)', content).group(0)
    baiduyun_psw = re.search(u'(?<=\u5bc6\u7801\uff1a).+', content).group(0)
    return baiduyun_url, baiduyun_psw

# 下载
def download(url):
    time, title, herf = get_new(url)
    baiduyun_url, baiduyun_psw = get_baiduyun_url_psw(herf)
    driver = webdriver.Chrome()
    driver.get(baiduyun_url)
    driver.refresh()
    elem = driver.find_element_by_id("accessCode")
    elem.send_keys(baiduyun_psw)
    elem.send_keys(Keys.RETURN)
    return 1


download("http://www.pdfzj.com/tag/微型计算机")

