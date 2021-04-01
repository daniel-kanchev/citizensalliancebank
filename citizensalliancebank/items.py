import scrapy


class Article(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
