import scrapy
from crawlers.items import Item


class LaptopSpider(scrapy.Spider):
    name = "laptop"
    allowed_domains = ["laptop.bg"]
    start_urls = ['''https://laptop.bg/search?utf8=%E2%9C%93&q=PlayStation+5''']

    def parse(self, response):
        
        for product in response.css('ul.products li article'):
            item = Item()
            
            itemName = product.css('''article a h2::text''').get()
            itemPrice = product.css('''article .price-container span.price::text''').get()
             
            if itemName == "Playstation 5":
                item = {
                    'site' : 'laptop.bg',
                    'availability': 'Available',
                    'price': itemPrice
                    }

                yield item
            
        