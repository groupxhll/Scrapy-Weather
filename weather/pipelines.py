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
        # 获取当前工作目录
        base_dir = os.getcwd()
        
        # 文件存在工作目录中data目录下的weather.txt文件内
        fiename = base_dir + '/data/weather.txt'

        # 以追加的方式打开文件，并写入对应的数据
        with open(fiename, 'a') as f:
            f.write(item['date'] + '\n')
            f.write(item['week'] + '\n')
            f.write(item['hightemperature'] + "℃ ~ " + item['lowtemperature'] + "℃" + '\n')
            f.write(item['weather'] + '\n')
            f.write(item['wind'] + '\n\n')

        # 下载图片
        with open(base_dir + '/data/' + item['date'] + '.png', 'wb') as f:
            f.write(requests.get("https:"+item['img']).content)

        return item

class W2json(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + '/data/weather.json'

        # 打开json文件，向里面以dumps的方式写入数据
        with codecs.open(filename, 'a') as f:
            # json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
            line = json.dumps(dict(item), ensure_ascii=False)
            f.write(line+'\n')

        return item

class W2mysql(object):
    def process_item(self,item,spider):
        
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
                sql = "INSERT INTO WEATHER(date,week,lowtemperature,hightemperature,weather,wind,img) VALUES (%s,%s,%s,%s,%s,%s,%s)"

                #执行sql语句
                #excute的第二个参数将sql缺省语句补全
                cursor.execute(sql,(item['date'],item['week'],item['lowtemperature'],item['hightemperature'],item['weather'],item['wind'],item['img']))

            # 提交本次插入的记录
            connection.commit()

        finally:
            # 关闭连接
            connection.close()

        return item
