import os.path

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

def _saveFile(fPath, content):
    with open(fPath, 'w') as f:
        f.write(content)

def _readWordList(fPath):
    words = ''
    with open(fPath, 'r') as wl: 
         words = wl.read().split()
    return words

class DemonPipeline(object):
    def __init__(self):
        basepath = os.path.dirname(__file__)
        self.urlsfilepath = os.path.abspath(os.path.join("..", "..", "..", basepath, "logs", "urls.txt"))
        self.omgfilepath = os.path.abspath(os.path.join("..", "..", "..", basepath, "logs", "omg.txt"))
        self.wlfilepath = os.path.abspath(os.path.join("..", "..", "..","..", basepath, "..", "wordlist.txt"))

    def process_item(self, item, spider):
#TODO: last url is not being correctly processed
#TODO: un-hardcode this damn url!
        for l in item['link']:
            print(l)
            #if "http://" not in l or "https://" not in l:
            #    l = "http://www.marinha.mil.br"+l
            _saveFile(self.urlsfilepath, l+"\n")

# Process page text content
        contentWords = [i.strip() for i in item['content']]
        wordList = _readWordList(self.wlfilepath)
#        any_in = lambda wordList, contentWords: any(i in contentWords for i in wordList)
        any_in = lambda a,b: any(i in b for i in a)
        if any_in(wordList, contentWords):
            _saveFile(self.omgfilepath, 'OMG!!!!! HACKED SITE!!!! GEEE MAN!!!' + ''.join(str(i) for i in item['link']))
           
        return item

    def close_spider(self, spider):
        self.urls.close()
        self.omg.close()
