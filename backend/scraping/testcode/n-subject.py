import re
from bs4 import BeautifulSoup
import webScraping
import datetime

webscrraping = webScraping.init({})
#resdata = webscrraping.targetsite('https://gall.dcinside.com/mgallery/board/lists?id=purikone_redive', 'get')
resdata = webscrraping.targetsite('https://gall.dcinside.com/mgallery/board/lists/?id=purikone_redive&sort_type=N&exception_mode=recommend&search_head=10&page=1', 'get')
soup = BeautifulSoup(resdata.get('data'), 'html.parser')
trdata = soup.select('tr.ub-content.us-post')
for tr in trdata:
    gallNum = tr.select('td.gall_num')
    gallNum = str(gallNum)
    gallNum = (re.sub('<.+?>', '', gallNum, 0).strip())
    gallSubject = tr.select('td.gall_subject')
    gallSubject = str(gallSubject)
    gallSubject = (re.sub('<.+?>', '', gallSubject, 0).strip())
    gallTit = tr.select('td.gall_tit > a')
    gallTit = str(gallTit[0])
    gallTit = (re.sub('<.+?>', '', gallTit, 0).strip())
    gallTiturl = tr.select('td.gall_tit > a')
    gallTiturl = gallTiturl[0].get('href')
    gallWriter = tr.select('td.gall_writer > span')
    gallWriter = str(gallWriter)
    gallWriter = (re.sub('<.+?>', '', gallWriter, 0).strip())
    gallDate = tr.select('td.gall_date')
    gallDate = str(gallDate)
    if gallDate.find('.') != -1:
        gallDate = gallDate
    else :
        now = datetime.datetime.now()
        gallDate = now.strftime('%m.%d')
    gallDate = (re.sub('<.+?>', '', gallDate, 0).strip())


    print(gallNum)
    print(gallSubject)
    print(gallTit)
    print(gallTiturl)
    print(gallWriter)
    print(gallDate)


#    tddata = tr.select('td.gall_num,td.gall_subject,td.gall_tit,td.gall_writer.ub-write,td.gall_date')
    """
    tddata = str(trdata.select('td.gall_num,.td.gall_subject,td.gall_tit.ub-word,td.gall_writer ub-write,td.gall_date'))
    tddata = re.sub('<.+?>', '', tddata, 0).strip()
    print(tddata)
    """
#tddata = str(tddata)
#print(tddata)
"""
    for td in tddata:
        td = str(td)
        if td.find('gall_num') != -1:
            gallNum = (re.sub('<.+?>', '', td, 0).strip())
            print('gall_num : ', gallNum)
        else:
            if td.find('gall_subject') != -1:
                gallSubject = (re.sub('<.+?>', '', td, 0).strip())
                print('gall_subject : ', gallSubject)
            else:
                if td.find('gall_tit') != -1:
                    gallTit = td
                    print(gallTit)
                    gallTit = gallTit.get('href')
                    print('gall_tit : ', gallTit)
                else:
                    if td.find('td.gall_writer.ub-write') != -1:
                        gallWriter = (re.sub('<.+?>', '', td, 0).strip())
                        print('gall_writer : ', gallWriter)
                    else:
                        if td.find('td.gall_date') != -1:
                            gallDate = (re.sub('<.+?>', '', td, 0).strip())
                            print('gall_writer : ', gallDate)
                        else:
                            print('gall_num None')
"""

#for trHtml in post:
#    tr = trHtml.select('td')
#    for td in tr:
#        print(":", td)

#""", gallCategory, gallSubject, gallSubjectUrl, nickname, date"""
