import scrapy

class Product(scrapy.Item):
    site = scrapy.Field()
    availability = scrapy.Field()
    price = scrapy.Field()
    
