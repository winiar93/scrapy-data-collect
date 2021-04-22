import scrapy

class Bring(scrapy.Spider):
    name = "quotes"
    start_urls = ['https://quotes.toscrape.com/']


    def parse(self, response):
        title = response.xpath('/html/body/div/div[2]/div[1]/div[2]/span[1]/text()').extract()
        #yield {"titletext":title}
        f = open('dane.txt','w')
        f.write(str(title)+"\n")
        f.close()


        
