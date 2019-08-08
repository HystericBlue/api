import webScraping
from bs4 import BeautifulSoup
headers = {}
webscrraping = webScraping.init(headers)
resdata = webscrraping.targetsite('https://gall.dcinside.com/mgallery/board/view/?id=purikone_redive&no=1097025', 'get')
print('resdata.code : ', resdata.get('code'))
soup = BeautifulSoup(resdata.get('data'), 'html.parser')
print(soup)                             

