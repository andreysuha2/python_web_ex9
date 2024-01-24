from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrap.spiders.quotes import QuotesSpider
from scrap.spiders.authors import AuthorsSpider

runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(QuotesSpider)
    yield runner.crawl(AuthorsSpider)
    reactor.stop()
    
if __name__ == "__main__":
    crawl()
    reactor.run()