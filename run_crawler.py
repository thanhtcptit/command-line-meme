import pymongo
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from meme_crawler.spiders.meme_spider import MemedroidSpider


process = CrawlerProcess(get_project_settings())

process.crawl(MemedroidSpider)
process.start()
