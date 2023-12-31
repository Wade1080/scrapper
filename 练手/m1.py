#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re01
import os
#需求：爬取糗事百科中糗图板块下所有的糗图图片
if __name__ == "__main__":
    #创建一个文件夹，保存所有的图片
    if not os.path.exists('./weiboLibs'):
        os.mkdir('./weiboLibs')

    url = 'https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D%E5%B1%B1%E5%A7%86'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

    }
    #使用通用爬虫对url对应的一整张页面进行爬取
    page_text = requests.get(url=url,headers=headers).text

    #使用聚焦爬虫将页面中所有的糗图进行解析/提取
    ex = '<div class="m-img-box">.*?<img src="(.*?)"</div>'
    img_src_list = re.findall(ex,page_text,re.S)
    # print(img_src_list)
    for src in img_src_list:
        #拼接出一个完整的图片url
        src = 'https:'+src
        #请求到了图片的二进制数据
        img_data = requests.get(url=src,headers=headers).content
        #生成图片名称
        img_name = src.split('/')[-1]
        #图片存储的路径
        imgPath = './weiboLibs/'+img_name
        with open(imgPath,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功！！！')


