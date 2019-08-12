import dbconfig
import datetime


dbContoroller = dbconfig.DBController('www.moodopa.com', 23306, 'webScraping', '!webScraping23', 'webScraping')


regdate = '2019-08-19 11:41:00'
convdate = datetime.datetime.strptime(regdate, '%Y-%m-%d %H:%M:%S').date()
print(convdate)

param = (600, 'dcinside', 'pricone', 'dd', 'testsample', 'test', convdate)


dbContoroller.insert_list(param)
