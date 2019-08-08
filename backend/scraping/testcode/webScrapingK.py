import webScraping

headers = {}
webscrraping = webScraping.init(headers)
data = webscrraping.targetsite('https://gall.dcinside.com/mgallery/board/view/?id=purikone_redive&no=1097025', 'get')
print('data : ', data)
