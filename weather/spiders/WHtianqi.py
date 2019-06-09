# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem

class WhtianqiSpider(scrapy.Spider):
    name = 'WHtianqi'
    # 允许爬取的域名
    allowed_domains = ['www.tianqi.com/wuhan']
    start_urls = ['https://www.tianqi.com/wuhan']

    def parse(self, response):
        # 建立items列表，用于保存每天的信息
        items = []
        # 获取包含所有天气信息的div
        sixday = response.xpath('/html/body/div[5]/div/div[2]/div[2]')

        # 循环选出每天的信息，并将其加入items中
        for i in range(0,6):
            # 申请一个WeatherItem类型，用于保存结果
            item = WeatherItem()

            # 通过xpath获取网站html中的节点信息，并将其存入item中
            #.xpath()[].extract(): 返回SelectorList(此处为sixday)中的第一个元素(如果list为空抛出异常)
            item['date'] = sixday.xpath('/html/body/div[5]/div/div[2]/div[2]/ul[1]/li/b/text()')[i].extract()
            item['week'] = sixday.xpath('/html/body/div[5]/div/div[2]/div[2]/ul[1]/li/span/text()')[i].extract()
            item['img'] = sixday.xpath('/html/body/div[5]/div/div[2]/div[2]/ul[1]/li/img/@src')[i].extract()
            item['hightemperature'] = sixday.xpath('/html/body/div[5]/div/div[2]/div[2]/div/ul/li/span/text()')[i].extract()
            item['lowtemperature'] = sixday.xpath('/html/body/div[5]/div/div[2]/div[2]/div/ul/li/b/text()')[i].extract()
            item['weather'] = sixday.xpath('/html/body/div[5]/div/div[2]/div[2]/ul[2]/li/text()')[i].extract()
            item['wind'] = sixday.xpath('/html/body/div[5]/div/div[2]/div[2]/ul[3]/li/text()')[i].extract()
            items.append(item)

        return items
