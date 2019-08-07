# from bs4 import BeautifulSoup
import requestURL
# import requests
#  URL = 'https://gall.dcinside.com/mgallery/board/view/?id=purikone_redive&no=1097025'
#
#  headers = {
#      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
#      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
#  }
#
#  data = {}
#
#  res = requests.get(URL, headers=headers, data=data)
#  html = res.text
#  soup = BeautifulSoup(html, 'html.parser')

url = 'https://gall.dcinside.com/mgallery/board/view/?id=purikone_redive&no=1097025'
headers = {}
data = {}
print('headers.size : ', len(headers))

# print(URL)
rUrl = requestURL.Url(headers)
html = rUrl.htmlObject("get", url, data)
print('ddd', html)