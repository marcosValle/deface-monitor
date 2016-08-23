from __future__ import absolute_import
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from demon.items import DemonItem
import os.path
import sys

class DemonSpider(CrawlSpider):
    name = "mar"
    allowed_domains = ["mil.br", "eb.br", "mar.br"]
    start_urls = [
        "http://www.marinha.mil.br"
    ]

    rules = (
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=()), callback='parse_items'),
    )

    def parse_items(self, response):
        item = DemonItem()
        item['link'] = response.xpath('//a/@href').extract()
        return item

