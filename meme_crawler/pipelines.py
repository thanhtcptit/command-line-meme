# -*- coding: utf-8 -*-
import pymongo

from scrapy.exceptions import DropItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MemeCrawlerPipeline(object):

    def __init__(self, mongo_server, mongo_port, mongo_db, mongo_coll):
        self.mongo_server = mongo_server
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db
        self.mongo_coll = mongo_coll

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(settings.get('MONGODB_SERVER'),
                   settings.get('MONGODB_PORT'),
                   settings.get('MONGODB_DB'),
                   settings.get('MONGODB_COLLECTION'))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(
            self.mongo_server, self.mongo_port)
        self.db = self.client[self.mongo_db]
        self.coll = self.db[self.mongo_coll]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        try:
            self.coll.insert(dict(item))
        except pymongo.errors.DuplicateKeyError as e:
            pass
        return item
