import unittest
from demon.spiders import demon
from demon import pipelines
from tests import fake_response_from_file
import json, os

class DemonSpiderTest(unittest.TestCase):
    def setUp(self):
        ''' Seting up class attributes to be used during the tests
        '''
        self.spider = demon.DemonSpider()
    
    def _test_item_results(self, results):
        ''' Testing the results of the test response.
        SUCCESS: items not empty
        '''
        permalinks = set()
        
        for key, value in results.items():
            self.assertIsNotNone(value)
            print(key, value)
    
    def test_parse(self):
        ''' Testing if the spider parsing is done correctly over a fake offline response
        '''
        results = self.spider.parse_items(fake_response_from_file("sample.html"))
        self._test_item_results(results)

class DemonPipelinesTest(unittest.TestCase):
    def setUp(self):
        self.pipeline = pipelines.DemonPipeline()
        self.spider = demon.DemonSpider()
        self.results = self.spider.parse_items(fake_response_from_file("sample.html"))
        self.item = self.pipeline.process_item(self.results, self.spider)

    def test_process_item(self):
        ''' Testing if items are being correctly processed
        '''
        self.assertIsNotNone(self.item)

    def test_urls_txt(self):
        ''' Testing if inspected urls are being correctly logged
        '''
        omgPath = 'demon/logs/omg.txt'
        #check if omg.txt is empty
        self.assertFalse(os.stat(omgPath).st_size)

    def test_hacked(self):
        '''Testing if accusing a simple hacked page
        '''
       
#Calling the tests
suite = unittest.TestLoader().loadTestsFromTestCase(DemonSpiderTest)
unittest.TextTestRunner(verbosity=2).run(suite)

pipeTest = unittest.TestLoader().loadTestsFromTestCase(DemonPipelinesTest)
unittest.TextTestRunner(verbosity=2).run(pipeTest)

