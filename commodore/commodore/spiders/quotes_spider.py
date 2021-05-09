import scrapy
import re

import smtplib
import os


class Bring(scrapy.Spider):
    name = "quotes"  # nazwa programu do uruchomienia w terminalu
    start_urls = ['https://www.olx.pl/oferty/q-commodore-64/?search%5Bfilter_float_price%3Afrom%5D=200&page=1'
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



    def send_mail(self):
        mailFrom = '...'

        mailTo = '...'

        mailSubject = 'Testowy mail oferty commodore '
        mailBody = ''' 
        '''

        message = '''From: {}
        Subject: {}
        testowy mail wyslany przez skrypt w pythonie {}
        '''.format(mailFrom, mailSubject, mailBody)



        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com',465)
            server.ehlo()
            server.login(user,password)
            server.sendmail(user,mailTo,message)
            server.close()
            print('mail sent')
        except:
            print('pojawił sie błąd')


process = Bring()

process.send_mail()