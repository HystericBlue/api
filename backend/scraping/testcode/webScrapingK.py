from bs4 import BeautifulSoup
import webScraping
import re
webscrraping = webScraping.init({})
resdata = webscrraping.targetsite('https://gall.dcinside.com/mgallery/board/lists?id=purikone_redive&exception_mode=recommend', 'get')
soup = BeautifulSoup(resdata.get('data'), 'html.parser')
trdata = soup.select('tr.ub-content.us-post')
for tr in trdata:
    tddata = tr.select('td.gall_num,.td.gall_subject,td.gall_tit.ub-word,td.gall_writer.ub-write,td.gall_date')
    """
    tddata = str(trdata.select('td.gall_num,.td.gall_subject,td.gall_tit.ub-word,td.gall_writer ub-write,td.gall_date'))
    tddata = re.sub('<.+?>', '', tddata, 0).strip()
    print(tddata)
    """
    for td in tddata:
        td = str(td)
        if td.find('gall_num') != -1:
            print('gall_num : ', td)
        else:
            print('gall_num None')
       # if td.find('gall_num') != -1:
       #     print('gall_num : ', td)
       # else:
       #     print('Not in gall_num')


