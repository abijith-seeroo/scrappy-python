from xml.sax import parse

import scrapy
from ..items import Webscrapyaccess



class CameraSpider(scrapy.Spider):
    name = 'camera_spider'
    start_urls = ['https://aperturent.com/accessories']

    def parse(self, response):
        access=Webscrapyaccess()
        all_div_quote=response.css('div.product-listing')
        for product in all_div_quote:
            product_name=product.css('div.product-listing-title a::text').get()
            product_desc=product.css('div.product-listing-description::text').get()
            product_image=product.css('div.product-listing-img-container img::attr(data-src)').get()
            product_see_more = product.css('div.product-listing-more-link a::attr(href)').get()

            if product_see_more:
                product_see_more = 'https://aperturent.com' + product_see_more
            access['product_name']=product_name
            access['product_desc']=product_desc
            access['product_image']=product_image
            access['product_see_more']=product_see_more

            yield access


