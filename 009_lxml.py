#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from lxml import etree
import requests

url = "https://movie.douban.com/chart"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}

response = requests.get(url, headers = headers)
html_str = response.content.decode()

# print(html_str)


html = etree.HTML(html_str)
# print(html)

url_list = html.xpath("//div[@class = 'indent']/div/table//div[@class = 'pl2']/a/@href")
# print(url_list)


img_list = html.xpath("//div[@class = 'indent']/div/table//a[@class = 'nbg']/img/@src")
# print(img_list)


ret1 = html.xpath("//div[@class = 'indent']/div/table")
print(ret1)

for table in ret1:
    item = {}
    item["title"] = table.xpath(".//div[@class = 'pl2']/a/text()")[0].replace("/","").strip()
    item["href"] = table.xpath(".//div[@class = 'pl2']/a/@href")[0]
    item["img"] = table.xpath(".//a[@class = 'nbg']/img/@src")[0]
    item["comment_num"] = table.xpath(".//span[@class = 'pl']/text()")[0]
    item["rating_num"] = table.xpath(".//span[@class = 'rating_nums']/text()")[0]
    print(item)

