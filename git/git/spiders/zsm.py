# -*- coding: utf-8 -*-
import scrapy


class ZsmSpider(scrapy.Spider):
    name = 'zsm'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/charliesmzsm']

    def start_requests(self):
        url = self.start_urls[0]
        temp = '_octo=GH1.1.1184247761.1558880441; _ga=GA1.2.1955078791.1558880454; _device_id=4de9f00746c74d2df8205c359298389d; user_session=vVbAzOr5swRZhXcIc1AASzGyV3jSVTduI4x8BJhC9pp64jno; __Host-user_session_same_site=vVbAzOr5swRZhXcIc1AASzGyV3jSVTduI4x8BJhC9pp64jno; logged_in=yes; dotcom_user=Charliesmzsm; has_recent_activity=1; tz=Asia%2FShanghai; _gat=1; _gh_sess=GWHSPuD%2Fh%2BvMsFYtcPwwDiRt6mlaSayCbVKpimPjsaiFGTtuCUw%2BK%2Fq%2FKuHBABO8gNNH50xXNP3XyJmnwkC1KromC04rFn191wFvgvmK%2BogwASFY1DE53YQBFFzVuwBxjTj96DXKSAsKzNsmKbrzEkc4jMBelXxdxDiAZSrQ773DI7T1egzUgmvRGWFIKuUP66JRAJQcpWWajcJ88CfwuLeElbJeZt2UFrBlSIF3NVvncC1MvXhpko6aH%2F7Ej9N6c62ao5z27%2BkkhN6q4xM4QPwwft79kEnvAAtuS9AH2jBb3rR89KDqiP7VMJO9Imhck3ZYVBXvumTCeEgbnoC40QnVQOP%2B0hDn563Pxy0iPRWVk5YfU8oBBKt30fVUAnW%2B1RsquyFUwFGdHSU474fpTZuMJjb3viCCcL2FaNN9m2GWv0KzPq0TcdQCU0HcnWw4CIWUTJjUkMEy6Rag2mYmf4scUu8LqmOCD8XnMvRp3LKZOMgEyZYzhRGj0a4%2FtbT6ppAZJU0yFBLaGVqtR2Ok1wY6BhDKWd77--i4s0g2I33Q2eu3aG--q0k8jwMTVnmGsZRSOXZ2Yg%3D%3D'
        coolies = {data.split('=')[0]:data.split('=')[-1]for data in temp.split('; ')}
        yield scrapy.Request(
            url=url,
            callback=self.parse,
            cookies=coolies
        )


    def parse(self, response):
        print(response.xpath('/html/head/title/text()').extract_first())
