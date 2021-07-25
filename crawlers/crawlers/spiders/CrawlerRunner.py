from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

process.crawl('laptop')
process.crawl('ardes')
process.crawl('ozone')
process.crawl('emag')
process.crawl('jarcomputers')
process.crawl('plesio')
process.crawl('polycomp')

process.start()
