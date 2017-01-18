#DeMon
##Open-source website defacement monitoring tool

This tool crawls through a user specified set of domains, starting from a user specified URL, following all the unrestricted links it founds. For each page it crawls, DeMon searches in a premade wordlist for malicious words that might indicate a defacement.

In the future it is intended to search also for defacement JS and images, according to a database. Also, automatic emails to admins are intended to be implemented soon. As a new feature, a graph shall be plotted with neo4j.

This tool was developed using Python3.5.2 and Scrapy and should work in versions 3.4+. It is strongly advised to create a virtualenvironment before using it or build the docker images.

So far this tool is being developed and **should not be trusted in production**.

Please feel free to add pull requests.

###How to use
Set your target URL:

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

* Phase 1
  * Fix urls.txt to store visited links
  * Finish wordlist detection code
  * Pass URL, domain and name as parameters
  * Implement Scrapy's e-mail functionalities
* Phase 2
  * Monitor images and codes (JS)
* Phase 3
  * Plot graphs using neo4j

###Disclaimer
This tool should not be used without authorization or against military/governmental websites.
