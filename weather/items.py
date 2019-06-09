# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item): # 希望获取的字段名
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field() # 日期
    week = scrapy.Field() # 星期
    img = scrapy.Field() # 图片
    hightemperature = scrapy.Field() # 当天最高温
    lowtemperature = scrapy.Field() # 当天最低温
    weather = scrapy.Field() # 天气
    wind = scrapy.Field() # 风向
    pass
