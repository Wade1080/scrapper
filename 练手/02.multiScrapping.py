# -*- coding: utf-8 -*-
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
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
# 构建第一页的多页集合，取出单页，查询target
# 构建第二页的多页集合，取出但也，查询tar所在地址


num = int(input('请输入要打印的页数: '))
# url = 'https://sc.chinaz.com/jianli/free.html'
# 先抓取前五页
'''无效写法 for 要放在最后面，不能放在str内，否则会失效'''
# url = ['https://sc.chinaz.com/jianli/']+['https://sc.chinaz.com/jianli/free_{}.html'.format(str(i) for i in range(2,num+1))]
url = ['https://sc.chinaz.com/jianli/']+['https://sc.chinaz.com/jianli/free_{}.html'.format(str(i)) for i in range(2, num+1)]
page_url1 = []
tar_list = []
tar_name_list = []
# 拿到的是第二页的汇总网页列表
def get_first_info(url):
    page_text1 = requests.get(url=url, headers=headers).text
    selector1 = etree.HTML(page_text1)
    # 大范围定位
    div_list = selector1.xpath('//div[@class="box col3 ws_block"]')

    for div_item in div_list:
        page_url1.append(div_item.xpath('./a/@href')[0])
    return page_url1



# 拿到的是压缩包的汇总网页列表
def get_second_info(page_url1):
    # 进入tar包所在页面
    for page_url2 in page_url1:
        page_text2 = requests.get(page_url2).text.encode('iso-8859-1').decode('utf-8')
        selector2 = etree.HTML(page_text2)
        tar_list.append(selector2.xpath('//ul[@class="clearfix"]/li[3]/a/@href')[0])
        tar_name_list.append(selector2.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')[0])
    return tar_list
def get_resouse(tar_list):
    for tar_url, tar_name in zip(tar_list, tar_name_list):
        tar_data = requests.get(url=tar_url, headers=headers).content
        tar_path = './tarLibs2/' + tar_name + '.zip'
        with open(tar_path, 'wb') as fp:
            fp.write(tar_data)
            print(tar_name +'\t 下载成功 ！！！')
if __name__ == '__main__':
    start = time.time()
    if not os.path.exists('./tarLibs2'):
        os.mkdir('./tarLibs2')
    # page_text1 = requests.get(url=url,headers=headers).text
    # selector1 = etree.HTML(page_text1)
    # # 大范围定位
    # div_list = selector1.xpath('//div[@class="box col3 ws_block"]')
    # page_url1 = []
    # for div_item in div_list:
    #     page_url1.append(div_item.xpath('./a/@href')[0])
    # print(page_url1,len(page_url1))
    # 跳转到对应url 抓取tar包的target
    # 获取第二个页面的地址列表
    for first_url in url:
        get_first_info(first_url)# 拿到了第二页链接的汇总
    get_second_info(page_url1)
    get_resouse(tar_list)
    end = time.time()
    delta = end - start
    print('下载结束，耗时:{} s'.format(delta))


















