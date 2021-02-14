import scrapy
from ..items import Assignment1Item


class NewsSpider(scrapy.Spider):
    name = 'news'
    page_number = 2
    start_urls = ['https://www.moneycontrol.com/news/tags/ongc.html/page-1/']

    def parse(self, response):
        item = Assignment1Item()
        code = response.css('li.clearfix')
        for tag in code:
            date = tag.xpath('span/text()').extract()
            headline = tag.xpath('h2/a/text()').extract()

            item['Date'] = date
            item['Headline'] = headline

            yield item

        new_url = 'https://www.moneycontrol.com/news/tags/ongc.html/page-'+str(NewsSpider.page_number)+'/'
        if NewsSpider.page_number < 102:
            NewsSpider.page_number += 1
            yield response.follow(new_url, callback=self.parse)
