# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobbleArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 文章标题
    title = scrapy.Field()
    # 内容摘要
    summary = scrapy.Field()
    # 发表日期
    publish_date = scrapy.Field()
    # 标签
    tag = scrapy.Field()
    pass
