# -*- coding: utf-8 -*-
import scrapy


class FlipkartSpiderSpider(scrapy.Spider):
    name = 'flipkart_spider'
    allowed_domains = ['flipkart.com']
    start_urls = ['http://flipkart.com/']

    def parse(self, response):
        pass
