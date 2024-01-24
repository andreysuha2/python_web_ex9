from scrap.store import authors_urls
import scrapy


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]
    
    def start_requests(self):
        print("Authors urls", authors_urls.urls)
        return super().start_requests()

    def parse(self, response):
        yield {}
