from bs4 import BeautifulSoup
import requestURL

url = 'https://gall.dcinside.com/mgallery/board/view/?id=purikone_redive&no=1097025'
headers = {}
data = {}

res = requests.get(URL, headers=headers, data=data)
html = res.text
soup = BeautifulSoup(html, 'html.parser')
post = soup.select('tr.ub-content.us-post')
i = 0
for trHtml in post:
    # print(trHtml)
    tr = trHtml.select('td')
    for td in tr:
        i = i+1
        print(i, ":", td)