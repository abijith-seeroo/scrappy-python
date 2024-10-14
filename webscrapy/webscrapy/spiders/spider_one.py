from xml.sax import parse

import scrapy
from ..items import WebscrapyItem



class QuotesSpider(scrapy.Spider):
    name = 'quotespider'
    page_number=2
    start_urls = ['https://quotes.toscrape.com/page/1/']

    def parse(self, response):
        items=WebscrapyItem()
        all_div_quote=response.css('div.quote')
        for quote in all_div_quote:
            title=quote.css('span.text::text').extract()
            author=quote.css('.author::text').extract()
            tags=quote.css('.tag::text').extract()
            items['title']=title
            items['author']=author
            items['tags']=tags

            yield items
        # next_page=response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page,callback=self.parse)

        next_page = 'https://quotes.toscrape.com/page/'+str(QuotesSpider.page_number)+'/'
        if QuotesSpider.page_number<11:
            QuotesSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)