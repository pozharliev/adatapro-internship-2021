import scrapy
from crawlers.items import Product

class LaptopSiteCrawler(scrapy.Spider):
    name = 'laptop'
    allowed_domains = ["laptop.bg"]
    start_urls = ['''https://laptop.bg/search?utf8=%E2%9C%93&q=PlayStation+5''']

    def parse(self, response):
        
        for product in response.css('ul.products li article'):
            item = Product()
            
            itemName = product.css('''article a h2::text''').get()
            itemPrice = product.css('''article .price-container span.price::text''').get()

            if "Playstation 5" in itemName:
                item = {
                    'site' : 'laptop.bg',
                    'availability': 'Available',                
                    'price': itemPrice
                    }
                yield item