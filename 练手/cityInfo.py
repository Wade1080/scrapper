# -*- coding: utf-8 -*-
import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
url = 'https://www.aqistudy.cn/historydata/'





if __name__=='__main__':
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    all_city = []
    hot_city = []
    # all_city_list = tree.xpath('//div[@class="bottom"]/ul')
    # for city_item in all_city_list:
    #     citys = city_item.xpath('./div[2]//a/text()')
    #     for city in citys:
    #         all_city.append(city)
    # print(all_city)
    # hot_city_list = tree.xpath('//div[@class="bottom"]/ul')
    # for city_item in hot_city_list:
    #     citys = city_item.xpath('./li/a/text()')
    #     for city in citys:
    #         hot_city.append(city)
    # print(hot_city)
    all_city_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    for li in all_city_list:
        city = li.xpath('./a/text()')[0]
        all_city.append(city)
    print(all_city)

    hot_city_list = tree.xpath('//div[@class="bottom"]/ul/li')
    for li in hot_city_list:
        city = li.xpath('./a/text()')[0]
        hot_city.append(city)
    print(hot_city)

    city_combine = []
    # 整合
    city_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li | //div[@class="bottom"]/ul/li')
    for li in city_list:
        city = li.xpath('./a/text()')[0]
        city_combine.append(city)
    print(city_combine)



