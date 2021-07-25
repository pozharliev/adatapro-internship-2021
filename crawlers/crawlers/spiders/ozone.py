import scrapy
from crawlers.items import Item


class LaptopSpider(scrapy.Spider):
    name = "ozone"
    allowed_domains = ["ozone.bg"]
    start_urls = ['''https://www.ozone.bg/landing/playstation-5/''']

    def parse(self, response):


            item = {
                "name": response.xpath("""//*[@id="product_addtocart_form"]/div/div[2]/h1""").get(),
                "price": response.xpath("""//*[@id="product-price-288701"]/span/text()[1]""").get()

            }

            yield item
