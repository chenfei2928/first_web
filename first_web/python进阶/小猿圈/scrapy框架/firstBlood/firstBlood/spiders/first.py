# -*- coding: utf-8 -*-
import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    allowed_domains = ['www.baidu.com']

    start_urls = ['http://www.baidu.com/','https://www.sogou.com/']

    def parse(self, response):
        print(response)
