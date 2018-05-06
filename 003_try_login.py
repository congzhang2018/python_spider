#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests

url = "https://space.bilibili.com/63132354/#/favlist?fid=95297278"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36","Cookie":"finger=14bc3c4e; rpdid=oopksxppqxdosikmxkkxw; sid=a3xb4w0m; DedeUserID=63132354; DedeUserID__ckMd5=1142a8124369117c; SESSDATA=2514061d%2C1527786116%2C31b28116; bili_jct=039a2a8c3be4e1b2b78d709eb5af9f71; buvid3=1C1574A9-B593-4AC4-9382-D400C9C19CD4103081infoc; fts=1525194129; UM_distinctid=1631ca7827d118f-05f0dadc403f0f-33617f06-1fa400-1631ca7827e346; LIVE_BUVID=43eb0ad7d056a9f008e8048a013a00ba; LIVE_BUVID__ckMd5=cdcf8202e6c8a035; user_face=https%3A%2F%2Fi0.hdslb.com%2Fbfs%2Fface%2Fbf6bf21a7b6d46ba57e0af5542ce87f7a9f87194.jpg; _cnt_dyn=undefined; _cnt_pm=0; _cnt_notify=0; uTZ=240; pgv_pvi=8662390784; _dfcaptcha=e56033f38f4be5b66f0defac700ce7d4; CNZZDATA2724999=cnzz_eid%3D74279219-1525190654-https%253A%252F%252Fwww.bilibili.com%252F%26ntime%3D1525545743"
}

response = requests.get(url, headers = headers)

with open("bilibili.html","w") as f:
    f.write(response.content.decode())