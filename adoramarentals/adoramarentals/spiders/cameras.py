import scrapy
from ..items import AdoramarentalsItem


class CameraSpider(scrapy.Spider):
    name = 'camera_spider'
    page_number = 25
    start_urls = ['https://www.adoramarentals.com/l/Cameras?startAt=0']

    def parse(self, response):
        camera = AdoramarentalsItem()
        all_div_quote = response.css('div.item')
        for product in all_div_quote:
            product_name = product.css('div.item-details h2 a::text').get().strip()
            product_image = product.css('div.item-img a img::attr(src)').get().strip()
            product_desc = product.css('div.pkg-includes ul li::text').getall()
            product_desc = [item.replace('\r\n', '').replace('\n', '').strip() for item in product_desc]

            if product_image:
                product_image = 'https://www.adoramarentals.com' + product_image
            camera['product_name'] = product_name
            camera['product_image'] = product_image
            camera['product_desc'] = product_desc

            yield camera

        next_page = "https://www.adoramarentals.com/l/Cameras?startAt=" + str(CameraSpider.page_number)
        if CameraSpider.page_number < 100:
            CameraSpider.page_number += 25
            yield response.follow(next_page, callback=self.parse)