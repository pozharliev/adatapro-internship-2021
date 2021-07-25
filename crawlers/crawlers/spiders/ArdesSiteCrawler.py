import scrapy
from crawlers.items import Product

class ArdesSiteCrawler(scrapy.Spider):
    name = "ardes"
    allowed_domains = ["ardes.bg"]
    start_urls = ['''https://ardes.bg/products?q=Playstation+5''']
    
    def parse(self,response):
        for product in response.xpath("""//*[@class="product"]"""):
            item = Product()
            itemName = product.xpath(""".//div[@class="title"]//span/text()""").get()
            itemPrice = product.xpath(""".//span[@class="price-num"]/text()""").get()
            
            if "Playstation 5" in itemName:
                item = {
                    'site' : "ardes.bg",
                    'availability': 'Available',                
                    'price': itemPrice
                    }
            yield item

        # Да се ограничи до по малко количество страници
        next_page = response.css(".next a::attr(href)").get()                        
        if next_page is not None:                                    
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


            
        