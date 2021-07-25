import scrapy
from crawlers.items import Product

class PlesioCrawler(scrapy.Spider):
    name = 'plesio'
    allowed_domains = ["plesio.bg"]
    start_urls = ['''https://plesio.bg/search.html?keyword=playstation&catalogue=undefined&mode=searchlist''']

    def parse(self, response):

        for product in response.xpath("""//*[@class="productListItem"]"""):
            item = Product()
            itemName = product.xpath(""".//div[@class="productTitle"]//b/text()""").get()
            itemPrice = product.xpath(""".//div[@class="class="productPrice"]/text()""").get()


            if "PlayStation 5" in itemName:
                item = {
                    'name' : 'itemName',
                    'availability': 'Available',
                    'price': itemPrice
                    }
                yield item
