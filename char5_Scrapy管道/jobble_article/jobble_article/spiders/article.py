import scrapy


class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://jobbole.com/']

    def parse(self, response):
        pass
