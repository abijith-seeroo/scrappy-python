# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AdoramarentalsItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    product_desc = scrapy.Field()
    product_image = scrapy.Field()
    # product_see_more = scrapy.Field()
