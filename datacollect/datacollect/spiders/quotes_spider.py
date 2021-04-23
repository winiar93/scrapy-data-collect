import scrapy

class Bring(scrapy.Spider):
    name = "quotes"  # nazwa programu do uruchomienia w terminalu
    start_urls = ['https://www.olx.pl/oferty/q-commodore-64/']


    def parse(self, response):
        for data in response.css('wrap'):
            yield {
                "name": data.css('strong::text').get(),
                "price": data.css('p.price').get(),
                "link" : data.css('a.marginright5.link.linkWithHash.detailsLink').attrib['href']
            }
        # f = open('dane.txt','a')
        # f.write(str(title)+"\n")
        # f.close()


        
