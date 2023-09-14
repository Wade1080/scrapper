# -*- coding: utf-8 -*-
import requests
from lxml import etree
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
url = 'https://bj.58.com/ershoufang/'
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
item_list = tree.xpath('//section[@class="list"]/div')
fp = open('title.txt','w',encoding='utf-8')
for item in item_list:
    title = item.xpath('./a/div[2]//h3/text()')
    print(title)
    # fp.write(str(title)+"\n")



