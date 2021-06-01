import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import LianjiahouseItem


class HouseSpider(CrawlSpider):
    name = 'house'
    allowed_domains = ['lianjia.com']
    start_urls = ['http://bj.lianjia.com/ershoufang/']

    rules = (
        Rule(LinkExtractor(allow=r'/ershoufang/pg\d{12}.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = LianjiahouseItem()
        # 二手房名称
        item['house_name'] = response.css('title::text').extract_first().replace(' ', '')
        # 所在小区
        item['community_name'] = response.css('.communityName a::text').extract_first()
        # 链家编号
        item['house_record'] = response.css('.houseRecord .info::text').extract_first()
        # 总价
        # 有改动
        item['total_amount'] = response.css('.price .total::text').extract_first()

        # 房屋信息
        # 单价
        item['unit_price'] = response.css('.unitPriceValue::text').extract_first()
        # 建筑总面积
        item['area_total'] = response.xpath('//div[@class="base"]//ul/li[3]/text()') \
            .re_first('\d+.\d+')
        # 使用面积
        item['area_use'] = response.xpath('//div[@class="base"]//ul/li[5]/text()') \
            .re_first('\d+.\d+')
        # 房屋类型
        item['house_type'] = response.xpath('//div[@class="base"]//ul/li[1]/text()') \
            .extract_first()
        # 装修情况
        item['sub_info'] = response.xpath('//div[@class="base]//ul/li[7]/text()') \
            .extract_first()
        # 供暖方式
        item['heating_method'] = response.xpath('//div[@class="base"]//ul/li[11]/text()') \
            .extract_first()
        # 产权
        item['house_property'] = response.xpath('//div[@class="base"]//ul/li[13]/text()') \
            .extract_first()
        # 楼层
        item['floor'] = response.xpath('//div[@class="base"]//ul/li[2]/text()') \
            .extract_first()
        # 总楼层
        item['total_floors'] = response.xpath('//div[@class="base"]//ul/li[2]/text()') \
            .re_first(r'\d+')
        # 是否有电梯
        item['is_left'] = response.xpath('//div[@class="base"]//ul/li[12]/text()') \
            .extract_first()
        # 户梯比例
        item['left_rate'] = response.xpath('//div[@class="base"]//ul/li[10]/text()') \
            .extract_first()

        # 挂牌时间
        item['release_date'] = response.xpath('//div[@class="transaction"]//ul/li[i]'
                                              '/span[2]/text()').extract_first()
        # 最后交易时间
        item['last_trade_time'] = response.xpath('//div[@class="transaction"]//ul/li[3]'
                                                 '/span[2]/text()').extract_first()
        # 房屋使用年限
        item['house_years'] = response.xpath('//div[@class="transaction"]//ul/li[5]'
                                             '/span[2]/text()')
        # 房屋抵押信息,抵押信息中有空格及换行符，先通过replace()将空格去掉，再通过strip()将换行符去掉
        item['pawn'] = response.xpath('//div[@class="transaction"]//ul/li[7]/span[2]'
                                      '/text()').extract_first().replace(' ', '').strip()
        # 交易权属
        item['trade_property'] = response.xpath('//div[@class="transaction"]//ul/li[2]'
                                                '/span[2]/text()').extract_first()
        # 房屋用途
        item['house_usage'] = response.xpath('//div[@class="transaction"]//ul/li[4]'
                                             '/span[2]/text()').extract_first()
        # 产权所有
        item['property_own'] = response.xpath('//div[@class="transaction"]//ul/li[6]'
                                              '/span[2]/text()').extract_first()
        # 图片url
        item['images_urls'] = response.css('.smallpic > li::attr(data-pic)').extract()

        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        yield item
