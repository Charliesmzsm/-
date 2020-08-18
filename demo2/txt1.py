from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
from urllib.error import HTTPError, URLError
import re

# 爬取院校信息
def findScdhoolInfo(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'lxml')
        schoolInfo = bsObj.findAll("table", {"class":"ch-table"})
    except AttributeError as e:
        return None
    return schoolInfo

# 处理信息为需要的信息
def handleSchoolInfo(info):
    if info == None:
        print("没有院校信息")
    else:
        school_list = []
        for item in info:
            list = item.findAll("tr")
            for x in list:
                school = x.findAll("td")
                if len(school):
                    school_list.append(school[0:3])
                else:
                    continue
        for item in school_list:
            school_name = item[0].get_text().strip()
            school_shengfen = item[1].get_text()
            shcool_belong = item[2].get_text()
            print(school_name)

shcoolInfo = findScdhoolInfo("https://yz.chsi.com.cn/sch/search.do?start=1")
handleSchoolInfo(shcoolInfo);

print("爬取完成")



# html = urlopen("https://www.cnblogs.com/ladyzhu/p/9617567.html")#括号内的是需要爬取的网址地址
# bsObj = BeautifulSoup(html.read())
#
# print(bsObj.prettify())