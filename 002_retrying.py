#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from retrying import retry
import requests

headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 \
           (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

@retry(stop_max_attempt_number = 3) # running code for 3 times

def _parse_url(url):
    print("*"*100)
    response = requests.get(url, headers = headers, timeout = 5)
    return response.content.decode()

def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return html_str

if __name__ == '__main__':
    url = "http://www.baidu.com"
    url1 = "www.baidu.com"
    # print(parse_url(url)[:100])
    print(parse_url(url1))