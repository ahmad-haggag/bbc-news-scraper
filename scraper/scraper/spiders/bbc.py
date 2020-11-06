import logging
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BbcNewsItem


class BbcSpider(CrawlSpider):
    name = 'bbc'
    start_urls = ['https://www.bbc.com/']

    rules = [
        Rule(LinkExtractor(allow='https://www.bbc.com/news'),
             callback='parse_news', follow=True)
    ]


    def parse_news(self, response):
        '''
        DESCRIPTION:
        -----------
        * This function is the callback for parsing URL content response,


        PARAMETERS:
        ----------
            1. the response to be parsed
        '''

        if response.status == 200:
            url = response.url

            item = BbcNewsItem()
            item['url'] = url
            item['headline'] = response.xpath('//h1[@id="main-heading"]/text()').extract_first()

            logging.info(' Item : ' + str(item))

            return item
