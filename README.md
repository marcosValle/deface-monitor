#DeMon
##Open-source website defacement monitoring tool

This tool was developed using Python3.5.2 and Scrapy. It is strongly advised to create a virtualenvironment before using it.

So far this tool is being developed and **should not be trusted in production**.

Please feel free to add pull requests.

###How to use
First, run some integrity tests:

    $python3 tests.py
    test_parse (__main__.DemonSpiderTest)
    Testing if the spider parsing is done correctly over a fake offline response ... ok
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.003s
    
    OK

Now set your target URL:

    /deface_monitor/monitor/demon/spiders$ vim demon
    class DemonSpider(CrawlSpider):
        name = "NAME_HERE"
        allowed_domains = ["DOMAINS_HERE"]
        start_urls = [
                "FQDN_URL_HERE"
        ]


Finally, run, baby, run:

    $python3 run.py
    
###TODO
* Finish wordlist detection code
* Pass URL, domain and name as parameters
* Implement Scrapy's e-mail functionalities
* Monitor images and codes

###Disclaimer
This tool should not be used without authorization or against military/governmental websites.
