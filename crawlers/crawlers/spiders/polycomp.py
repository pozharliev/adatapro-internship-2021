import scrapy
from crawlers.items import Product

class PolycompCrawler(scrapy.Spider):
    name = 'polycomp'
    allowed_domains = ["polycomp.bg"]
    start_urls = ['''https://polycomp.bg/poly/search''']

    def parse(self, response):

        for product in response.xpath("""//*[@class="product"]"""):
            item = Product()
            itemName = product.xpath(""".//div[@class="tooltip"]//b/text()""").get()
            itemPrice = product.xpath(""".//div[@class="class="class="product_price"]/text()""").get()


            if "Playstation 5" in itemName:
                item = {
                    'name' : 'itemName',
                    'availability': 'Available',
                    'price': itemPrice
                    }
                yield item
