# -*- coding: utf-8 -*-
import scrapy


class Zsm2Spider(scrapy.Spider):
    name = 'zsm2'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def parse(self, response):
        token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()
        post_data = {
            "commit": "Sign in",
            "authenticity_token":token,
            "ga_id": "1955078791.1558880454",
            "login": "572996481@qq.com",
            "password": "Charlie52678",
            "webauthn-support": "supported",
            "webauthn-iuvpaa-support": "supported",
            "timestamp": "1597937750438",
            "timestamp_secret": "2d02fb9a4cf0b78c78e74fa4bb5ad3a07b0e8bdb07951f0434d4aeebeac00799"
        }
        print(post_data)
        #针对登录发送post 请求
        yield scrapy.FormRequest(
            url='https://g ithub.com/session',
            callback=self.after_login,
            formdata=post_data
        )
    def after_login(self,res):
        yield scrapy.Request(
            url='https://github.com/charliesmzsm',
            callback=self.check_login
        )
    def check_login(self,res):
        print(res.xpath('/html/head/title/text()').extract_first())
