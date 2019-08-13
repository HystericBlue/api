from bs4 import BeautifulSoup
import webScraping
import re


class ArticleScr:
    def init(self, gallNum, gallTiturl, count=0, flags=0):
        self.gallNum = gallNum
        self.gallTiturl = gallTiturl
        self.count = count
        self.flags = flags

    def articleParser(self):
        webscrraping = webScraping.init({})
        resdata = webscrraping.targetsite(self.gallTiturl, 'get')
        soupB = BeautifulSoup(resdata.get('data'), 'html.parser')
        postArticle = soupB.select('div.view_content_wrap')
        for divHtml in postArticle:
            category = divHtml.select('h3.title.ub-word > span.title_headtext')
            subject = divHtml.select('h3.title.ub-word > span.title_subject')
            article = divHtml.select('div.writing_view_box > div> div')
            self.articleMap = {'category':category, 'subject':subject, 'article':article }
        return self.articleMap

#    def converter(self):
#        resdata = str(self.articleMap[])
#        resdata = (re.sub(self.gallNum, self.gallTiturl, resdata, self.count).strip())
#        return resdata