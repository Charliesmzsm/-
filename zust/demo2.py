import requests
from lxml import etree
url = 'https://hr.163.com/job-list.html'

res = requests.get(url)

html = etree.HTML(res.content)
end = html.xpath('//*[@id="root"]/section/div[2]/div/div[2]/div[2]/div/div/div')
if end == []:
    end = html.xpath('//div[@class="posi-list-card"]/div[@class="list-card-content"]/div/div[1]')

print(end)