# -*- coding: utf-8 -*-
import requests
from lxml import etree
headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
url = 'https://sc.chinaz.com/jianli/free_2.html'

def getInfo(url):
    page_text = requests.get(url=url,headers=headers).text.encode('iso-8859-1').decode('utf-8')
    selector = etree.HTML(page_text)
    item_list = selector.xpath('//div[@class="box col3 ws_block"]')
    for item in item_list:
        content = item.xpath('./p/a/text()')[0]
        name_list.append(content)


num = int(input('请输入要爬虫的页数，从2开始：'))  # 将输入转换为整数类型
url_list = ['https://sc.chinaz.com/jianli/']+['https://sc.chinaz.com/jianli/free_{}.html'.format(str(i)) for i in range(2, num+1)]
name_list = []
print(url_list)
for url in url_list:
    getInfo(url)

print(name_list,len(name_list))

# url = 'https://sc.chinaz.com/jianli/free_4.html'
# if __name__ == '__main__':
#     page_text = requests.get(url=url,headers=headers).text.encode('iso-8859-1').decode('utf-8')
#     selector = etree.HTML(page_text)
#

#
# def geturl(num):
#     url_list = [['https://sc.chinaz.com/jianli/']+['https://sc.chinaz.com/jianli/free_{}.html'.format(str(i)) for i in range(2, num)]]
#     return url_list








# item_list = selector.xpath('/div[@class="main_list jl_main masonry"]')
# print(item_list)
# name_list = []
# for item in item_list:
#     name = item.xpath('./p/a/text()')[0]
#     name_list.append(name)
# print(name_list)
#
# if __name__ == '__main__':
#     num = int(input('请输入要爬虫的页数，从2开始：'))  # 将输入转换为整数类型
#     url_list = geturl(num)
#     for url in url_list:
#         name_list = getInfo(str(url))



