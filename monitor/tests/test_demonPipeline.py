import unittest
from demon.spiders import demon
from demon import pipelines
from tests import fake_response_from_file
import json, os

class DemonPipelinesTest(unittest.TestCase):
    def setUp(self):
        self.spider = demon.DemonSpider()
        self.results = self.spider.parse_items(fake_response_from_file("sample.html"))
        self.pipeline = pipelines.DemonPipeline()
        self.item = self.pipeline.process_item(self.results, self.spider)

    def test_process_item(self):
        ''' Testing if items are being correctly processed
        '''
        self.assertIsNotNone(self.item)

    def test_urls_txt(self):
        ''' Testing if inspected urls are being correctly logged
        '''
        urlsPath = 'demon/logs/urls.txt'
        #check if urls.txt is empty
        self.assertNotEqual(os.stat(urlsPath).st_size, 0)

        with open(urlsPath) as f:
            content = f.readlines()
            print(content)

    def test_hacked(self):
        '''Testing if accusing a simple hacked page
        '''
        omgPath = 'demon/logs/omg.txt'

        with open(omgPath) as f:
            content = f.readlines()
            print(content)

        #check if omg.txt shows an alert
        self.assertNotEqual(os.stat(omgPath).st_size, 0)

#Calling the tests
pipeTest = unittest.TestLoader().loadTestsFromTestCase(DemonPipelinesTest)
unittest.TextTestRunner(verbosity=2).run(pipeTest)

