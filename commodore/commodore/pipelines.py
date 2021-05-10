# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from email.message import EmailMessage
import smtplib
from email.message import EmailMessage

from itemadapter import ItemAdapter


class CommodorePipeline:
    def process_item(self, item, spider):

        return item

