from bs4 import BeautifulSoup
import webScraping


class ArticleScr:
    def __init__(self, gallnum, galltiturl):
        self.params = {'gallnum': gallnum, 'galltiturl': galltiturl}
        print('listTableInit params: ', self.params)

    def articleparser(self):
        webscrrapinga = webScraping.init({})
        resdata = webscrrapinga.targetsite(self.params, 'get')
        soup = BeautifulSoup(resdata.get('data'), 'html.parser')
        postarticle = soup.select('div.view_content_wrap')
        for divhtml in postarticle:
 #           category = divHtml.select('h3.title.ub-word > span.title_headtext')
 #           subject = divHtml.select('h3.title.ub-word > span.title_subject')
            self.article = divhtml.select('div.writing_view_box > div> div')
 #           self.articleMap = {'category': category, 'subject': subject, 'article': article }
            print(self.article)
