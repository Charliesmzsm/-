import requests
import json
import logging
logging.captureWarnings(True)
import certifi
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko Core/1.70.3766.400 QQBrowser/10.6.4163.400',
    'Cookie':'UM_distinctid=17167a59ad40-069cfe58516d8a-335e4e71-144000-17167a59ad529a; ezproxy=Azr5yml7sYLT0HH; cookies=44785.4929.7938.0000; ASP.NET_SessionId=gqhdkc55smavfb55k3hxge45; iPlanetDirectoryPro=AQIC5wM2LY4Sfcw1Rbz9WOQazn%2FWo4l433kZhXtc5Os%2FkQ0%3D%40AAJTSQACMDE%3D%23; ezproxy=AyZ3knn5VF19QBI'
}
url = 'http://jwxt.zust.edu.cn.ez.zust.edu.cn/cjcx.aspx?xh=xx012&xm=%E6%9D%A8%E5%B9%BF%E5%AE%87&gnmkdm=N120305'

res = requests.post(url,headers = header)
print(res.text)