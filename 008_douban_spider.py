#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from parse import parse_url
import json

class DoubanSpider:

    def __init__(self):

        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288&_=1525565883135"


    def get_content_list(self, html_url):
        dict_data = json.loads(html_url)
        content_list = dict_data["subject_collection_items"]
        total = dict_data["total"]
        return content_list, total


    def save_content_list(self, content_list):
        with open("douban.json","a") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii = False))
                f.write("\n")

        print("save sucessful!!")

    def run(self):

        num = 0
        total = 100

        while num < total + 18:

            start_url = self.temp_url.format(num)

            html_str = parse_url(start_url)

            content_list, total = self.get_content_list(html_str)

            self.save_content_list(content_list)

            num += 18

if __name__ == '__main__':

    douban = DoubanSpider()
    douban.run()
