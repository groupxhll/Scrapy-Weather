# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
import json
import codecs
import pymysql

class WeatherPipeline(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        fiename = base_dir + '/data/weather.txt'

        with open(fiename, 'a') as f:
            f.write(item['date'] + '\n')
            f.write(item['week'] + '\n')
            f.write(item['hightemperature'] + "℃ ~ " + item['lowtemperature'] + "℃" + '\n')
            f.write(item['weather'] + '\n')
            f.write(item['wind'] + '\n\n')

        with open(base_dir + '/data/' + item['date'] + '.png', 'wb') as f:
            f.write(requests.get(item['img']).content)

        return item

class W2json(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + '/data/weather.json'

        with codecs.open(filename, 'a') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)

        return item
class W2mysql(object):
    def process_item(self,item,spider):
        #将item里的数据拿出来
        """date = item['date']
        week = item['week']
        temperature = item['temperature']
        weather = item['weather']
        wind = item['wind']
        img = item['img']"""
        #WhtianqiSpider.parse()
        #和本地的scrapyDB数据库连接

        connection = pymysql.connect(
            host='localhost',
            user='root',
            passwd='Hzcmysql_0627',
            db='scrapyDB',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                #创建更新值的sql语句
                sql = "INSERT INTO WEATHER(date,week,lowtemperature,hightemperature,weather,wind,img) VALUES 
                      (%s,%s,%s,%s,%s,%s,%s)"

                #执行sql语句
                #excute的第二个参数可以将sql缺省语句补全，一般以元组格式
                cursor.execute(sql,(item['date'],item['week'],item['lowtemperature'],item['hightemperature'],item['weather'],item['wind'],item['img']))

            connection.commit()

        finally:
            connection.close()

        return item
