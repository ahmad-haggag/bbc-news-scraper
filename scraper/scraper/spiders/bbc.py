import logging
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BbcNewsItem
from readability import Document
import html2text
from goose3 import Goose


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
            item['headline'] = response.xpath('//title/text()').extract_first()
            item['authors'] = response.xpath("//meta[ @ property = 'article:author'").extract()

            item['text'] = self.get_article_text(response_html=response.text)

            logging.info(' Item : ' + str(item))

            return item

    def get_article_text(self, response_html):
        '''
               DESCRIPTION:
               -----------
               * This function cleanse the page of superfluous content such as advertising and HTML

               PARAMETERS:
               ----------
                   1. html response body
               '''

        doc = Document(response_html)
        article_html = Document(doc.content()).summary()
        h = html2text.HTML2Text()
        h.ignore_links = True
        article_text = h.handle(article_html)
        article_text = article_text.replace('\r', ' ').replace('\n', ' ').strip()
        return article_text
