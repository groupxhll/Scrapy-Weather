## Scrapy-Weather项目说明文档
#### a)项目信息  
- 利用scrapy框架爬取天气网站的数据，得到武汉地区近七天的天气信息。  
- 将爬取到的数据分别保存到txt、json、以及mysql数据库中。   

#### b)作者信息及详细的分工和完成情况  
|name|work|result|  
|--- |----| ---  |
|刘亭玉|数据的爬取|完成   |
|何志琛|数据写入数据库|完成  |
|刘玥滢|修改代码|完成  |
|许智超|测试代码|完成  |
#### c)开发环境，/运行环境
&emsp;&emsp;开发环境：window 10 Anconda spider  
&emsp;&emsp;运行环境： windows PowerShell  Mac OS
#### d)系统架构/关键技术
- scrapy框架  
- 用xpath定位网页中天气信息的位置  
- 编写PIPELINE用于处理爬到的数据

#### e)使用的方法/资源   
&emsp;&emsp;[scrapy文档](https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html#id4)    
&emsp;&emsp;[xpath w3school教程](http://www.w3school.com.cn/xpath/index.asp)    
&emsp;&emsp;[twist等相关包的下载资源](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pywin32)  

f)其他
效果预览
```
06月09日
星期日
31℃ ~ 24℃
阴
东风

06月10日
星期一
33℃ ~ 21℃
多云转晴
东北风

06月11日
星期二
31℃ ~ 22℃
多云
东风

06月12日
星期三
31℃ ~ 20℃
阴
东风

06月13日
星期四
32℃ ~ 20℃
晴
东北风

06月14日
星期五
32℃ ~ 21℃
多云
东风

06月15日
星期六
33℃ ~ 22℃
阴
东南风


```
