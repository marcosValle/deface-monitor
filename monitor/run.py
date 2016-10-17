import scrapy
from scrapy.crawler import CrawlerProcess
from demon.spiders import demon

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(demon.DemonSpider())
process.start() # the script will block here until the crawling is finished
