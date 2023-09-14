#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    urls = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    keyword = input('请输入城市:')
    param = {
        'cname':'',
        'pid':'',
        'keyword': keyword,
        'pageIndex': 1,
        'pageSize': '10'
    }
    response = requests.post(url=urls,params=param,headers=headers)
    list_data = response.text
    fileName = keyword + '.txt'
    with open(fileName,'w',encoding='utf-8') as file:
        file.write(list_data)
    print('Finished')
