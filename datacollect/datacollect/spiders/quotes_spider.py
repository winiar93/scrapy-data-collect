import scrapy

class Bring(scrapy.Spider):
    name = "quotes"  # nazwa programu do uruchomienia w terminalu
    start_urls = ['https://www.olx.pl/oferty/q-commodore-64/']


    def parse(self, response):
        for data in response.css('.wrap'):
            yield {
                "name":data.css('strong::text').get(),
                "price": data.css('p.price').get(),
                #"link": data.css('table.offers.redesigned.userobserved-list.space.h3.a.listHandler.table.offers.redesigned.space.h3.a').attrib['href']
                "link":data.xpath('//*[@id="offers_table"]/tbody/tr[12]/td/div/table/tbody/tr[1]/td[2]/div/h3/a/@href').extract()
            }
        # f = open('dane.txt','a')
        # f.write(str(title)+"\n")
        # f.close()


        
