#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os.path

import requests
import re
import json
if __name__ == "__main__":
    if not os.path.exists('./songLibs'):
        os.mkdir('./songLibs')
    url = 'https://www.jitashe.org/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

    }
    response = requests.get(url=url,headers=headers)
    list_data = response.text
    ex = '<div class="tablist-item-a">.*?<img src="(.*?)">'
    url_list = re.findall(ex,list_data,re.S)
    ex_1 = '<div class="item-text item-title"><a href=".*?" title="(.*?)" target="_self">'
    name_list = re.findall(ex_1,list_data,re.S)
    print(url_list)


    for url,image_name in zip(url_list,name_list):
        image_data = requests.get(url=url,headers=headers).content

        imgPath = './songLibs/' + image_name
        with open(imgPath,'wb') as fp:
            fp.write(image_data)
            print(image_name,'下载成功！！！')



    # fp = open('./douban.json','w',encoding='utf-8')
    # json.dump(list_data,fp=fp,ensure_ascii=False)
    # print('over!!!')