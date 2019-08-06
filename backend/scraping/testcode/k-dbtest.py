import dbconfig

dbContoroller = dbconfig.DBController('www.moodopa.com', 23306, 'webScraping', '!webScraping23', 'webScraping')
count = dbContoroller.select_list_count()
print(count)
