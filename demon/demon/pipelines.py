import os.path

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DemonPipeline(object):
    def __init__(self):
        basepath = os.path.dirname(__file__)
        urlsfilepath = os.path.abspath(os.path.join("..", "..", "..", basepath, "urls.txt"))
        omgfilepath = os.path.abspath(os.path.join("..", "..", "..", basepath, "omg.txt"))
        wlfilepath = os.path.abspath(os.path.join("..", "..", "..","..", basepath, "..", "wordlist.txt"))

        self.urls = open(urlsfilepath, 'a')
        self.omg = open(omgfilepath, 'a')
        self.wl = open(wlfilepath, 'r')  

    def process_item(self, item, spider):
#TODO: last url is not being correctly processed
        for l in item['link']:
            if "http://" not in l or "https://" not in l:
                l = "http://www.marinha.mil.br"+l
            self.urls.write(l+"\n")

# Process page text content
        for c in item['content']:
            for w in self.wl:
                if w in c:
                    self.omg.write('OMG!!!!! HACKED SITE!!!! GEEE MAN!!!')
#                self.omg.write(item['link'])
        return item


    def close_spider(self, spider):
        self.urls.close()
        self.omg.close()
