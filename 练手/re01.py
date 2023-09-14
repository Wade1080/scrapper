import re01
key1 = "safjahjpyt170honfhaspython"
re.findall('python',key1)[0]
key2='<html><h1>hello world<h1><html>'
b = re.findall('<h1>(.*)<h1>',key2)[0]
print(re.findall('\d+', key1))

string = '12344567'
print(re.findall('1230?4*567$',string))
p1 = '<Html>1390813</html>'
print(re.findall('<[Hh]tml>(.*)</[Hh]tml>', p1))
web = 'https:www.baidu.com'
print(re.findall('h.*?\.', web))

keyy = 'saas and sas and saaas'
print(re.findall('sa{1,2}s', keyy))