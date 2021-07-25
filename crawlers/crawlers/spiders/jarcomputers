import scrapy
#from twisted.crawler import
from scrapy.items import Item
from twisted.internet import reactor
from scrapy.utils.log import configure_logging



class JarcomputersSiteCrawler(scrapy.spider):
    name = "jarcomputers"
    allowed_domains = ["jarcomputers.com"]
    start_urls = ["""https://www.jarcomputers.com/search?q=Playstation+5&ref=&btn=++"""]

    def parse(self, response):

        for product in response.css("ul.items li aritcle"):
            item = Item()

            itemName = item.css("""article a h2::text""").get()

            itemPrice=item.xpath(""".//td[@class="product-new-price"]/text()""").get()




            if "PS5" or "PlayStation 5" in itemName:
                item = {"site": "jarcomputers.com", "price":itemPrice,"availability":"Available"}

        yield item
