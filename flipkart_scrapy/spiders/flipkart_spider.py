# -*- coding: utf-8 -*-
import scrapy
from ..items import FlipkartScrapyItem

class FlipkartSpiderSpider(scrapy.Spider):
    name = 'flipkart_spider'
    allowed_domains = ['flipkart.com']
    start_urls = ['https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=clp_metro_expandable_1_3.metroExpandable.METRO_EXPANDABLE_Mi_mobile-phones-store_ZHYC957RFL_wp3&fm=neo%2Fmerchandising&iid=M_08a4f72d-5561-4395-8e25-39c2ef816925_2.ZHYC957RFL&ppt=clp&ppn=mobile-phones-store']

    def parse(self, response):
        items = FlipkartScrapyItem()

        all_div_mobile=response.css('._1UoZlX')
        
        for mobile in all_div_mobile:
            product_name=mobile.css('._3wU53n::text').extract()
            product_price=mobile.css('._2rQ-NK::text').extract()
            product_rating=mobile.css('._2_KrJI .hGSR34').css('::text').extract()
        
            items['product_name']=product_name
            items['product_price']=product_price
            items['product_rating']=product_rating

            yield items     
