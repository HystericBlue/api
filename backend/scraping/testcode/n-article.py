from bs4 import BeautifulSoup
import requests
URL = 'https://gall.dcinside.com/mgallery/board/view/?id=purikone_redive&no=1097025'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
}

data = {}

res = requests.get(URL, headers=headers, data=data)
html = res.text
soup = BeautifulSoup(html, 'html.parser')
post = soup.select('div.view_content_wrap')

for divHtml in post:
    i = 0
    subject = divHtml.select('h3.title.ub-word')
    article = divHtml.select('div.writing_view_box > div')
    i = i + 1
    print(i, ":", subject)
    i = i + 1
    print(i, ":", article[1])
