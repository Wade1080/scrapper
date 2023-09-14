import requests
import json
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    url = 'https://www.zhipin.com/web/geek/job?query=java&city=101280100'
    params = {
        'scene': '1',
        'query': 'java',
        'city': '101280100',
        'experience': '',
        'payType': '',
        'partTime': '',
        'degree': '',
        'industry': '',
        'scale': '',
        'stage': '',
        'position': '',
        'jobType': '',
        'salary': '',
        'multiBusinessDistrict': '',
        'multiSubway': '',
        'page': '{}'.format(str(i) for i in range(1,10)),
        'pageSize': '30'
    }
    json_ids = requests.get(url=url,headers=headers,data=params)
    print(json_ids)
