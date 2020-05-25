# -*- coding: utf-8 -*-
import scrapy


class QiuSpider(scrapy.Spider):
    name = 'qiu'
    allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        # 解析作者的名称+ 段子内容
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        all_data = []
        for div in div_list:
            #author= div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            author= div.xpath('./div[1]/a[2]/h2/text()').extract_first()

            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)

            dic = {'author':author,'content':content
            }
        print(all_data)
        return all_data


