# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem

class WhtianqiSpider(scrapy.Spider):
    name = 'WHtianqi'
    allowed_domains = ['https://www.tianqi.com/wuhan']
    start_urls = ['https://www.tianqi.com/wuhan']

    def parse(self, response):
        items = []
        sixday = response.xpath('/html/body/div[5]/div/div[2]/div[2]')
        for i in range(0,6):
            for day in sixday:
                item = WeatherItem()
                date = day.xpath('/html/body/div[5]/div/div[2]/div[2]/ul[1]/li/b/text()')[i].extract()

            item['date'] = date

            item['week'] = day.xpath('/html/body/div[5]/div/div[2]/div[2]/ul[1]/li/span/text()')[i].extract()
            item['img'] = day.xpath('/html/body/div[5]/div/div[2]/div[2]/ul[1]/li/img/@src')[i].extract()
            item['hightemperature'] = day.xpath('/html/body/div[5]/div/div[2]/div[2]/div/ul/li/span/text()')[i].extract()
            item['lowtemperature'] = day.xpath('/html/body/div[5]/div/div[2]/div[2]/div/ul/li/b/text()')[i].extract()
            item['weather'] = day.xpath('/html/body/div[5]/div/div[2]/div[2]/ul[2]/li/text()')[i].extract()
            item['wind'] = day.xpath('/html/body/div[5]/div/div[2]/div[2]/ul[3]/li/text()')[i].extract()
            items.append(item)

        return items
