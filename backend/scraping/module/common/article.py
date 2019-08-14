from bs4 import BeautifulSoup
import webScraping
import dbConn


class ArticleScr:
    def __init__(self, gallnum, galltiturl):
        self.gallnum = gallnum
        self.galltiturl = galltiturl
        self.params = {'gallnum': gallnum, 'galltiturl': galltiturl}
        print('listTableInit params: ', self.params)

    def articleparser(self):
        webscrrapinga = webScraping.init({})
        resdata = webscrrapinga.targetsite(self.galltiturl, 'get')
        soup = BeautifulSoup(resdata.get('data'), 'html.parser')
        postarticle = soup.select('div.view_content_wrap')
        for divhtml in postarticle:
            self.article = divhtml.select('div.writing_view_box > div> div')
            print(self.article)

            #dbconn = dbConn.CntnTableInit('www.moodopa.com', 23306, 'webScraping', '!webScraping23', 'webScraping')
            #dbconn.