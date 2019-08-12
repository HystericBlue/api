import re
from bs4 import BeautifulSoup
import webScraping
import datetime
import dbConn

webscrraping = webScraping.init({})
#resdata = webscrraping.targetsite('https://gall.dcinside.com/mgallery/board/lists?id=purikone_redive', 'get')
resdata = webscrraping.targetsite('https://gall.dcinside.com/mgallery/board/lists/?id=purikone_redive&sort_type=N&exception_mode=recommend&search_head=10&page=1', 'get')
soup = BeautifulSoup(resdata.get('data'), 'html.parser')
trdata = soup.select('tr.ub-content.us-post')
for tr in trdata:
    gallNum = tr.select('td.gall_num')
    gallNum = str(gallNum[0])
    gallNum = (re.sub('<.+?>', '', gallNum, 0).strip())
    gallSubject = tr.select('td.gall_subject')
    gallSubject = str(gallSubject[0])
    gallSubject = (re.sub('<.+?>', '', gallSubject, 0).strip())
    gallTit = tr.select('td.gall_tit > a')
    gallTit = str(gallTit[0])
    gallTit = (re.sub('<.+?>', '', gallTit, 0).strip())
    gallTiturl = tr.select('td.gall_tit > a')
    gallTiturl = gallTiturl[0].get('href')
    gallTiturl = 'https://gall.dcinside.com/mgallery/board' + gallTiturl
    gallWriter = tr.select('td.gall_writer > span')
    gallWriter = str(gallWriter[0])
    gallWriter = (re.sub('<.+?>', '', gallWriter, 0).strip())
    gallDate = tr.select('td.gall_date')
    gallDate = gallDate[0].get('title')
    gallDate = str(gallDate)


    print(gallNum)
    print(gallSubject)
    print(gallTit)
    print(gallTiturl)
    print(gallWriter)
    print(gallDate)

# DB connect

    dbconn = dbConn.init('www.moodopa.com', 23306, 'webScraping', '!webScraping23', 'webScraping')

    regdate = '2019-08-19 11:41:00'
    convdate = datetime.datetime.strptime(regdate, '%Y-%m-%d %H:%M:%S').date()
    print(convdate)

    param = (gallNum, 'dcinside', 'pricone', gallTiturl, gallTit, gallWriter, gallDate)

    dbconn.insert_list(param)

