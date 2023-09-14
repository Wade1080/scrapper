# -*- coding: utf-8 -*-
'''
# 单页操作
1. 解析当前页面，收集该页面的各数据的详情页地址
2. 跳转到简历详情页面收集tar包下载地址
3. 请求tar包地址，用二进制写入文件的方法将tar写入指定文件夹下
'''



import requests
from lxml import etree
import os


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
url = 'https://sc.chinaz.com/jianli/free.html'

if __name__ == '__main__':
    if not os.path.exists('./tarLibs'):
        os.mkdir('./tarLibs')
    page_text1 = requests.get(url=url,headers=headers).text
    selector1 = etree.HTML(page_text1)
    # 大范围定位
    div_list = selector1.xpath('//div[@class="box col3 ws_block"]')
    page_url1 = []
    for div_item in div_list:
        page_url1.append(div_item.xpath('./a/@href')[0])
    print(page_url1,len(page_url1))
    # 跳转到对应url 抓取tar包的target
    tar_list = []
    tar_name_list = []
    # 进入tar包所在页面
    for page_url2 in page_url1:
        page_text2 = requests.get(page_url2).text.encode('iso-8859-1').decode('utf-8')
        selector2 = etree.HTML(page_text2)
        tar_list.append(selector2.xpath('//ul[@class="clearfix"]/li[3]/a/@href')[0])
        tar_name_list.append(selector2.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')[0])
    print(tar_name_list)
    print(tar_list)
    # 访问对应的tar地址，用二进制写入
    for tar_url,tar_name in zip(tar_list,tar_name_list):
        tar_data = requests.get(url=tar_url,headers=headers).content
        tar_path = './tarLibs/' + tar_name +'.zip'
        with open(tar_path,'wb') as fp:
            fp.write(tar_data)

















