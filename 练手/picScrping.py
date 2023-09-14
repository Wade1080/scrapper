# -*- coding: utf-8 -*-
import requests
import os
from lxml import etree
if __name__ == '__main__':
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'http://pic.netbian.com/4Kdujia/'
    host ='https://pic.netbian.com/'

    page_text = requests.get(url=url,headers=headers).text.encode('ISO-8859-1')
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class="clearfix"]/li')
    for li in li_list:
        # print(li.xpath('./a/img/@src')[0].strip('/'))
        # img_url = url + li.xpath('./a/img/@src')[0].strip('/')
        img_url = host+li.xpath('./a/img/@src')[0]
        img_name = str(li.xpath('.//text()')).split()[0][2:]+'.jpg'
        img_path = './picLibs/' + img_name
        img_data = requests.get(url=img_url,headers=headers).content
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name+'下载成功')





    # for li in li_list:
    #     img_src = 'http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
    #     img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
    #
    #     # print(img_name,img_src)
    #     #请求图片进行持久化存储
    #     img_data = requests.get(url=img_src,headers=headers).content
    #     img_path = 'picLibs/'+img_name
    #     with open(img_path,'wb') as fp:
    #         fp.write(img_data)
    #         print(img_name,'下载成功！！！')
