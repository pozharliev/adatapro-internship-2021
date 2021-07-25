import scrapy
from crawlers.items import Product

class EmagSiteCrawler(scrapy.Spider):
    name = 'emag'
    allowed_domains = ["emag.bg"]
    start_urls = ['''https://www.emag.bg/search/playstation%205?ref=effective_search''']

    def parse(self, response):

        for product in response.xpath("""//*[@class="card-item js-product-data"]"""):
            item = Product()
            itemName = product.xpath(""".//div[@class="title"]//a/text()""").get()
            itemPrice = product.xpath(""".//div[@class="product-new-price"]/text()""").get()


            if "Playstation 5" in itemName:
                item = {
                    'site' : 'emag.bg',
                    'availability': 'Available',
                    'price': itemPrice
                    }
                yield item
