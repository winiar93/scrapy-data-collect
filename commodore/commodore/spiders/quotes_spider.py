import scrapy
import re
class Bring(scrapy.Spider):
    name = "quotes"  # nazwa programu do uruchomienia w terminalu
    start_urls = ['https://www.olx.pl/oferty/q-commodore-64/?search%5Bfilter_float_price%3Afrom%5D=200&page=1',
                  'https://www.olx.pl/oferty/q-commodore-64/?search%5Bfilter_float_price%3Afrom%5D=200&page=2',
                  'https://www.olx.pl/oferty/q-commodore-64/?search%5Bfilter_float_price%3Afrom%5D=200&page=2'
                  ]


    def parse(self, response):
        for data in response.css('div.offer-wrapper'):
            yield {
                "name":data.css('strong::text').get(),
                "price":(data.css('strong::text').extract()[1]).replace('zł',''),
                "link":data.css('a::attr(href)').extract()[0]


            }
        next_page = response.css('a.pageNextPrev::attr(href)').extract()[0]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
