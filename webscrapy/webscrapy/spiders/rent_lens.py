from xml.sax import parse

import scrapy
from ..items import WebscrapyLens



class LensSpider(scrapy.Spider):
    name = 'lensspider'
    start_urls = ['https://aperturent.com/lenses']

    def parse(self, response):
        lens=WebscrapyLens()
        all_div_quote=response.css('div.product-listing')
        for product in all_div_quote:
            product_name=product.css('div.product-listing-title a::text').get()
            product_desc=product.css('div.product-listing-description::text').get()
            product_image=product.css('div.product-listing-img-container img::attr(data-src)').get()
            product_see_more = product.css('div.product-listing-more-link a::attr(href)').get()

            if product_see_more:
                product_see_more = 'https://aperturent.com' + product_see_more
            lens['product_name']=product_name
            lens['product_desc']=product_desc
            lens['product_image']=product_image
            lens['product_see_more']=product_see_more

            yield lens


