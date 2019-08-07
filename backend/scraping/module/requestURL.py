from bs4 import BeautifulSoup
import requests

# requestURL.py
class Url:
    def __init__(self, headers):
        if len(headers) == 0:
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
            }
        else:
            self.headers = headers

    def htmlObject(self, method, url, data):
        if len(data) == 0:
            data = {}
        if method == 'post':
            res = requests.post(url, headers=self.headers, data=data)
        elif method == 'put':
            res = requests.put(url, headers=self.headers, data=data)
        elif method == 'delete':
            res = requests.delete(url, headers=self.headers, data=data)
        else:
            res = requests.get(url, headers=self.headers, data=data)
        htmlstring = res.text
        return htmlstring
        print('==> htmlObject End')