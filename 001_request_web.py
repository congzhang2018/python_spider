#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

# # Get requests
# url = "http://www.baidu.com"
# headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 \
#            (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
# response = requests.get(url, headers = headers, timeout = 3)
#
# # response.encoding = "utf-8"
# # print(response.text)
#
# print(response.content.decode())
# # response.content.decode("gbk")




# Post requests
url = "http://fanyi.baidu.com/basetrans"

query_string = {"query": "人生苦短，我用Python",
                "from": "zh",
                "to": "en"}
headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 \
            (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
           "Referer": "https: // fanyi.baidu.com /"}

response = requests.post(url, data = query_string, headers = headers)

# print(response)
print(response.content.decode())
print(response.request.url)
print(response.url)
print(response.request.headers)
print(response.headers)

