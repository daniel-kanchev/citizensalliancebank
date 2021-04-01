import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from datetime import datetime
from citizensalliancebank.items import Article


class citizensalliancebankSpider(scrapy.Spider):
    name = 'citizensalliancebank'
    start_urls = ['https://www.citizensalliancebank.com/resources/news/']

    def parse(self, response):
        content_containters = response.xpath('//div[contains(@class, "panel-collapse")]')
        content = []
        for item in content_containters:
            content.append(item.xpath('.//text()').getall())

        titles = response.xpath('//a[@data-toggle="collapse"]//h4/text()').getall()
        titles = [title.strip() for title in titles]

        for i, title in enumerate(titles):
            item = ItemLoader(Article())
            item.default_output_processor = TakeFirst()

            item.add_value('title', title)
            body = [text.strip() for text in content[i] if text.strip() and '{' not in text]
            body = "\n".join(body).strip()
            item.add_value('content', body)

            yield item.load_item()
