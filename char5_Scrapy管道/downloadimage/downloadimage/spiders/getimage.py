import scrapy


class GetimageSpider(scrapy.Spider):
    name = 'getimage'
    allowed_domains = ['qidian.com']
    start_urls = ['http://qidian.com/']

    def parse(self, response):
        pass
