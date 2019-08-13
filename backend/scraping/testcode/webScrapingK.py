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
        """
        if td.find('gall_num') != -1:
            td = str(td)
            print('gall_num : ', re.sub('<.+?>', '', td, 0).strip())
        else:
            print(len(td))
        """
        print(len(td))
        if (len(td) != 1 ):
            title = td.select('b')
            atag = td.find('a')
            print(atag.get('href'))
            print(title)



