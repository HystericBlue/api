import re
from bs4 import BeautifulSoup
import webScraping
import article
import dbConn

webscrraping = webScraping.init({})
#resdata = webscrraping.targetsite('https://gall.dcinside.com/mgallery/board/lists?id=purikone_redive', 'get')
resdata = webscrraping.targetsite('https://gall.dcinside.com/mgallery/board/lists/?id=purikone_redive&sort_type=N&exception_mode=recommend&search_head=10&page=1', 'get')
soup = BeautifulSoup(resdata.get('data'), 'html.parser')
trdata = soup.select('tr.ub-content.us-post')

for tr in trdata:
    gallnum = tr.select('td.gall_num')
    gallnum = str(gallnum[0])
    gallnum = (re.sub('<.+?>', '', gallnum, 0).strip())
    gallsubject = tr.select('td.gall_subject')
    gallsubject = str(gallsubject[0])
    gallsubject = (re.sub('<.+?>', '', gallsubject, 0).strip())
    title = tr.select('td.gall_tit > a')
    title = str(title[0])
    title = (re.sub('<.+?>', '', title, 0).strip())
    galltiturl = tr.select('td.gall_tit > a')
    galltiturl = galltiturl[0].get('href')
    galltiturl = 'https://gall.dcinside.com' + galltiturl
    gallwriter = tr.select('td.gall_writer > span')
    gallwriter = str(gallwriter[0])
    gallwriter = (re.sub('<.+?>', '', gallwriter, 0).strip())
    galldate = tr.select('td.gall_date')
    galldate = galldate[0].get('title')
    galldate = str(galldate)

    print(gallnum)
    #    dbconn = dbConn.ListTableInit('www.moodopa.com', 23306, 'webScraping', '!webScraping23', 'webScraping')
    #    numchecked = dbconn.numcheck(gallnum)
    #    print('numchecked : ', numchecked)
    #    if numchecked == 0:
    #        param = (gallnum, 'dcinside', 'pricone', galltiturl, galltit, gallwriter, galldate)
    #        dbconn.insert(param)
    #    else:
    #        print('저장된 데이터 입니다.')

    # Article
    articlex = article.ArticleScr(gallnum, gallsubject)
    articleparser = articlex.articleparser()