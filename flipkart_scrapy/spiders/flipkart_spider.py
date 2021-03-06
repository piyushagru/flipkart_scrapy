# -*- coding: utf-8 -*-
import scrapy
from ..items import FlipkartScrapyItem

class FlipkartSpiderSpider(scrapy.Spider):
    name = 'flipkart_spider'
    page_number = 2
    start_urls = [
            'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=clp_metro_expandable_1_3.metroExpandable.METRO_EXPANDABLE_Mi_mobile-phones-store_ZHYC957RFL_wp3&fm=neo%2Fmerchandising&iid=M_8cc5a5f4-0d90-4876-a2eb-676e5b27f8aa_2.ZHYC957RFL&ppt=clp&ppn=mobile-phones-store&page1%2F=&page=1'
        ]

    def parse(self, response):
        items = FlipkartScrapyItem()

        # all_div_mobile=response.css('._1UoZlX')
        all_div_mobile=response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_1UoZlX", " " ))]')
        
        for mobile in all_div_mobile:
            product_name=mobile.css('div._3wU53n::text').extract()
            product_price=mobile.css('div._2rQ-NK::text').extract()
            product_rating=mobile.css('span._2_KrJI .hGSR34').css('::text').extract()
        
            items['product_name']=product_name
            items['product_price']=product_price
            items['product_rating']=product_rating

            yield items     

        # next_page = response.css('._3fVaIS::attr(href)').get()
        # if next_page is not None:
        #         yield response.follow(next_page, callback = self.parse)
        next_page='https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=clp_metro_expandable_1_3.metroExpandable.METRO_EXPANDABLE_Mi_mobile-phones-store_ZHYC957RFL_wp3&fm=neo%2Fmerchandising&iid=M_8cc5a5f4-0d90-4876-a2eb-676e5b27f8aa_2.ZHYC957RFL&ppt=clp&ppn=mobile-phones-store&page1%2F=&page='+str(FlipkartSpiderSpider.page_number)
        
        # next_page=response.urljoin(next_page)

        if FlipkartSpiderSpider.page_number <= 20:
                FlipkartSpiderSpider.page_number += 1
                yield response.follow(next_page, callback = self.parse)
