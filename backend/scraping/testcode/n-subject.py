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

    param = (gallNum, 'dcinside', 'pricone', gallTiturl, gallTit, gallWriter, gallDate)
    dbconn = dbConn.init('www.moodopa.com', 23306, 'webScraping', '!webScraping23', 'webScraping')
    
    numchecked = dbconn.gallnum_check(gallNum)
    if numchecked == 0:
        dbconn.insert_list(param)
    else:
        print('저장된 데이터 입니다.')

        # Article
    resdataB = webscrraping.targetsite(gallTiturl, 'get')
    print(resdataB)
    soupB = BeautifulSoup(resdataB.get('data'), 'html.parser')
    postArticle = soupB.select('div.view_content_wrap')

    for divHtml in postArticle:
        print(divHtml)
        i = 0
        category = divHtml.select('h3.title.ub-word > span.title_headtext')
        subject = divHtml.select('h3.title.ub-word > span.title_subject')
        article = divHtml.select('div.writing_view_box > div> div')
        #       articleIa = divHtml.select('div.writing_view_box > div > div > img')
        #       articleText = article[1].text.strip()
        #       articleImage = articleIa[0].get('src')
        print("category :", category)
        print("subject :", subject)
#       print("article text :", articleText)
#       print("article img :", articleImage)
#       print("article raw :", article[1])

