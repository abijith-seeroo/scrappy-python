from xml.sax import parse

import scrapy
from ..items import Webscrapyvideo



class VideoSpider(scrapy.Spider):
    name = 'videospider'
    start_urls = ['https://aperturent.com/video']

    def parse(self, response):
        video=Webscrapyvideo()
        all_div_quote=response.css('div.product-listing')
        for product in all_div_quote:
            product_name=product.css('div.product-listing-title a::text').get()
            product_desc=product.css('div.product-listing-description::text').get()
            product_image=product.css('div.product-listing-img-container img::attr(data-src)').get()
            product_see_more = product.css('div.product-listing-more-link a::attr(href)').get()

            if product_see_more:
                product_see_more = 'https://aperturent.com' + product_see_more
            video['product_name']=product_name
            video['product_desc']=product_desc
            video['product_image']=product_image
            video['product_see_more']=product_see_more

            yield video


