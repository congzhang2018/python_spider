#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from lxml import etree

class QiubaiSpider:

    def __init__(self):

        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}

    def get_url_list(self):

        url_list = [self.url_temp.format(i) for i in range(1,14)]
        return url_list

    def parse_url(self, url):

        print("now parsing:", url)
        response = requests.get(url, headers = self.headers)
        return response.content.decode()

    def get_content_list(self, html_str):

        html = etree.HTML(html_str)
        div_list = html.xpath("//div[@id = 'content-left']/div")
        content_list = []
        for div in div_list:
            item = {}
            item["author_name"] = div.xpath(".//h2/text()")[0].strip() if len(div.xpath(".//h2/text()"))>0 else None
            item["content"] = div.xpath(".//div[@class = 'content']/span/text()")
            item["content"] = [i.strip() for i in item["content"]]
            item["stats_vote"] = div.xpath(".//span[@class = 'stats-vote']/i/text()")
            item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"])>0 else None
            item["stats_comments"] = div.xpath(".//span[@class = 'stats-comments']//i/text()")
            item["stats_comments"] = item["stats_comments"][0] if len(item["stats_comments"])>0 else None
            item["img"] = div.xpath(".//div[@class = 'thumb']//img/@src")
            item["img"] = "https:" + item["img"][0] if len(item["img"])>0 else None
            content_list.append(item)
        return content_list

    def save_content_list(self, content_list):

        with open("qiubai.text","a") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii = False))
                f.write("\n")
        print("Save successful!!")

    def run(self):

        url_list = self.get_url_list()

        for url in url_list:
            html_str = self.parse_url(url)
            content_list = self.get_content_list(html_str)
            self.save_content_list(content_list)

if __name__ == '__main__':

    qiubai = QiubaiSpider()
    qiubai.run()

