import requests,openpyxl
from bs4 import BeautifulSoup
import time
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "温州房价信息"

tittle = ["小区名称", "居室和面积", "地址", "价格"]
sheet.append(tittle)
# url
# 请求头
def getInfo(page):
    url = 'https://wz.newhouse.fang.com/house/s/b9'+ str(page) +'/'

    header = {
        "Referer": url,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
    }
    # 发送http
    res = requests.get(url, headers=header)
    res.encoding = "gb2312"

    # 解析
    soup = BeautifulSoup(res.text, "html.parser")
    divs = soup.find_all("div", class_="nlc_details")
    # 小区
    for div in divs:
        list1 = []
        list1.append(div.find_all("div", class_="nlcd_name")[0].a.text.strip())
        list1.append(div.find_all("div", class_="house_type clearfix")[0].a.text.strip())
        list1.append("".join(div.find_all("div", class_="address")[0].a.text.split()))
        s = "".join(div.find_all("div", class_="nhouse_price")[0].text.split())
        s = s[:s.find("/")]
        list1.append(s)
        sheet.append(list1)

for x in range(1,15):
    getInfo(x)
    print("第%d页正在下载"%(x))
workbook.save("index13房源信息.xlsx")

# 处理数据
