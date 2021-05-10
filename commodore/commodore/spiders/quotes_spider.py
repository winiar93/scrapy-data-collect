import logging
import re
from os import path
from datetime import date

import scrapy
from scrapy.crawler import CrawlerProcess
import smtplib
import smtplib
from email.message import EmailMessage
import os.path

import os
from ..items import CommodoreItem
FILE_NAME = 'oferty-{}'.format(date.today())


class Bring(scrapy.Spider):
    name = "quotes"  # nazwa programu do uruchomienia w terminalu
    start_urls = ['https://www.olx.pl/oferty/q-commodore-64/?search%5Bfilter_float_price%3Afrom%5D=200&page=1']

    custom_settings = {
        'FEEDS': {
            FILE_NAME: {
                'format': 'csv'
            }
        }
    }

    def parse(self, response):

        items = CommodoreItem()

        for data in response.css('div.offer-wrapper'):

            name = data.css('strong::text').get()
            link = data.css('a::attr(href)').extract()[0]
            price = (data.css('strong::text').extract()[1]).replace('zł', '')


            items['name'] = name
            items['link'] = link
            items['price'] = price


            yield items

        next_page = response.css('a.pageNextPrev::attr(href)').get()
        if next_page is not None:

            yield response.follow(next_page, callback=self.parse)

    def close(self,reason):
        logging.info('Data processing finished')


        msg = EmailMessage()
        msg['From'] = ''
        msg['To'] = ''
        msg['Subject'] = 'oferty commodore'
        msg.set_content('c64 offers from scraper')
        file_path = os.path.dirname(__file__)
        if file_path != "":
            os.chdir(file_path)
        f = open('../../{}'.format(FILE_NAME))
        data = f.read()
        msg.add_attachment(data, filename='{}.csv'.format(FILE_NAME))
        # smtplib.SMTP('smtp.gmail.com', 587)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

            server.ehlo()
            server.login('***', '****')
            server.send_message(msg)
            server.close()
            print('mail sent')
        except:
            print('found connection error')




