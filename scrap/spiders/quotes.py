import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "quotes.json"}

    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            yield {
                "quote": quote.xpath("span[@class='text']/text()").get(),
                "tags": quote.xpath("div[@class='tags']/a/text()").extract(),
                "author": quote.xpath("span/small/text()").get()
            }
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)
