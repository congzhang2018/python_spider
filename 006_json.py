#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import json

# Post requests
url = "http://fanyi.baidu.com/basetrans"

query_str = input("Please write the transfer Chinese:")
query_string = {"query": query_str,
                "from": "zh",
                "to": "en"}
headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 \
            (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
           "Referer": "https: // fanyi.baidu.com /"}

response = requests.post(url, data = query_string, headers = headers)

# print(response)
# print(response.content.decode())
# print(response.request.url)
# print(response.url)
# print(response.request.headers)
# print(response.headers)

html_str = response.content.decode()

dict_ret = json.loads(html_str)
print(dict_ret)
print(type(dict_ret))
ret =dict_ret["trans"][0]["dst"]
print("transfer result:", ret)