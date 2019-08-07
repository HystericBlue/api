from bs4 import BeautifulSoup
import requests

# requestURL.py
class Url:
    def __init__(self, url, headers):
        if headers == '' and headers == null:
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
            }
        else:
            self.headers = headers
        self.url = url

    def htmlObject(self):
        sql = 'SELECT COUNT(1) FROM TARGET_LIST WHERE 1 = 1'
        self.curs.execute(sql)
        row = self.curs.fetchone()
        # print('row ==> ', row)
        # rows = self.curs.fetchall()
        #  print(rows)
        # for row in rows:
        #     print(row)
        self.conn.close()
        return row