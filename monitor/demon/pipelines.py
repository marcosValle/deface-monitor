import os.path

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DemonPipeline(object):
    def __init__(self):
        basepath = os.path.dirname(__file__)
        urlsfilepath = os.path.abspath(os.path.join("..", "..", "..", basepath, "logs", "urls.txt"))
        omgfilepath = os.path.abspath(os.path.join("..", "..", "..", basepath, "logs", "omg.txt"))
        wlfilepath = os.path.abspath(os.path.join("..", "..", "..","..", basepath, "..", "wordlist.txt"))

        self.urls = open(urlsfilepath, 'w')
        self.omg = open(omgfilepath, 'w')
        self.wl = open(wlfilepath, 'r')  

    def process_item(self, item, spider):
#TODO: last url is not being correctly processed
#TODO: un-hardcode this damn url!
        for l in item['link']:
            if "http://" not in l or "https://" not in l:
                l = "http://www.marinha.mil.br"+l
            self.urls.write(l+"\n")

# Process page text content
        contentWords = [i.strip() for i in item['content']]
        wordList = self.wl.read().split()
#        any_in = lambda wordList, contentWords: any(i in contentWords for i in wordList)
        any_in = lambda a,b: any(i in b for i in a)
        if any_in(wordList, contentWords):
            self.omg.write('OMG!!!!! HACKED SITE!!!! GEEE MAN!!!')
            self.omg.write(''.join(str(i) for i in item['link']))
        return item


    def close_spider(self, spider):
        self.urls.close()
        self.omg.close()
