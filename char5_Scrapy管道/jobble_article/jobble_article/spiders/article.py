import scrapy
from ..items import JobbleArticleItem

class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://jobbole.com/licai/qihuo/']

    def parse(self, response):
        all_post = response.css(".list-item")
        for post in all_post:
            item = JobbleArticleItem()
            item['title'] = post.css('.dan::text').extract_first()
            item['summary'] = post.css('.content-desc shuang p::text').extract_first()
            # 根据正则表达式提取日期
            item['publish_date'] = post.css('.about-left p::text').re_first(
                'r\d{4}/\d{2}/d{2}')
            # tag标签可能有多个,因此不需要获取第一个值，保存列表即可
            item['tag'] = post.xpath(".//title-tag/text()").extract()
            yield item

        # 检查是否有下一页url，如果有，调用parse
        next_page = response.css('a1::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse)
