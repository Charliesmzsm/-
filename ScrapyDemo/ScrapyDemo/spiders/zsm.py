# -*- coding: utf-8 -*-
import scrapy
from ScrapyDemo.items import ScrapydemoItem

# scrapy gensipder zsm baidu.com
# >scrapy crawl zsm
class ZsmSpider(scrapy.Spider):
    name = 'zsm'
    allowed_domains = ['https://github.com/']
    start_urls = ['https://hr.163.com/position/list.do']


    def parse(self, response):
        # 定义对于网站的相关操作
        node_list = response.xpath('//table[@class="position-tb"]/tbody/tr')

        for num, node in enumerate(node_list):
            if num % 2 == 0:
                item = ScrapydemoItem()
                item['name'] = node.xpath('./td[1]/a/text()').extract_first()
                item['link'] = node.xpath('./td[1]/a/@href').extract_first()
                item['dep'] = node.xpath('./td[2]/text()').extract_first()
                item['category'] = node.xpath('./td[3]/text()').extract_first()
                item['type'] = node.xpath('./td[4]/text()').extract_first()
                item['address'] = node.xpath('./td[5]/text()').extract_first()
                item['num'] = node.xpath('./td[6]/text()').extract_first().strip()  # 去除空格
                item['date'] = node.xpath('./td[7]/text()').extract_first()
                # 构建详情页面的请求
                detail_url = response.urljoin(item['link'])
                print(detail_url)
                yield scrapy.Request(
                    url=detail_url,
                    callback=self.parse_detail,
                    meta={'item':item}
                )



                # yield item
        part_url = response.xpath('//div[@class="g-layout"]/div[2]/div/a[last()]/@href').extract_first()
        # print(part_url)
        if part_url != 'javascript:void(0)':
            next_url = response.urljoin(part_url)
            print(next_url)
            yield scrapy.Request(
                url=next_url,
                callback=self.parse
            )

    def parse_detail(self,response):
        # 将meta 传参 提取剩余字段数据
        item = response.meta['item']
        item['duty']=response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/text()').extract()
        item['require']=response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/text()').extract()
        # 返回给引擎
        yield item