import os.path

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DemonPipeline(object):
    def __init__(self):
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join("..", "..", "..", basepath, "urls.txt"))

        self.file = open(filepath, 'a')

    def process_item(self, item, spider):
        for l in item['link']:
            self.file.write(l.encode('utf-8')+'\n')

        return item

    def close_spider(self, spider):
        self.file.close()
