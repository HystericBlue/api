import dbConn
import datetime


dbconn = dbConn.init('www.moodopa.com', 23306, 'webScraping', '!webScraping23', 'webScraping')


regdate = '2019-08-19 11:41:00'
convdate = datetime.datetime.strptime(regdate, '%Y-%m-%d %H:%M:%S').date()
print(convdate)

param = (600, 'dcinside', 'pricone', 'dd', 'testsample', 'test', convdate)


dbconn.insert_list(param)
