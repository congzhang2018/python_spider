#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

session = requests.session()

post_url = ""

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}

post__data = {}

session.post()

url = ""
response = session.get(url, headers = headers)

with open("bilibili5.html","w") as f:
    f.write(response.content.decode())
