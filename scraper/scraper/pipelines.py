# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import logging

from scrapy.exceptions import DropItem


class MongoDBPipeline:
    collection_name = 'bbc_news'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        # pull in information from settings.py
        return cls(
            mongo_uri=crawler.settings.get('MONGODB_URL'),
            mongo_db=crawler.settings.get('MONGODB_DB')

        )

    def open_spider(self, spider):
        # opening db connection
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        # clean up when spider is closed
        self.client.close()

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if data == 'text' and not data:
                valid = False
                logging.error(" URL %s dropped ", str(item['url']))
                raise DropItem(" URL Missing {0}!".format(data))
        if valid:
            self.db[self.collection_name].insert(dict(item))
            logging.info("  URL  %s  added to database ", str(item['url']))
        return item
