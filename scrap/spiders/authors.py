from scrap.store import authors_urls
import scrapy


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "authors.json"}
    
    def start_requests(self):
        for url in authors_urls.urls:
            yield scrapy.Request(f"https://quotes.toscrape.com{url}/", callback=self.parse)

    def parse(self, response):
        author = response.xpath("/html//div[@class='author-details']")
        yield {
            "fullname": author.xpath("h3[@class='author-title']/text()").get(),
            "born_date": author.xpath("//span[@class='author-born-date']/text()").get(),
            "born_location": author.xpath("//span[@class='author-born-location']/text()").get(),
            "description": author.xpath("div[@class='author-description']/text()").get()
        }
