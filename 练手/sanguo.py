import requests
from bs4 import BeautifulSoup
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text  = requests.get(url=url,headers=headers).text
    soup = BeautifulSoup(page_text,'lxml')
    li_list = soup.select('book-mulu > ul > li')
    for li in li_list:
        title = li.a.string
        detail_url = li.a["href"]

