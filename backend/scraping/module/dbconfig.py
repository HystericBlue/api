import pymysql


# dbconfig.py
class DBController:
    def __init__(self, host, port, user, password, db):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8')
        self.curs = self.conn.cursor()

    def select_list_count(self):
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

#   def insert_total(self,total):
#       sql = 'INSERT INTO entire_nodes (count_of_nodes) VALUES (%s)'
#       self.curs.execute(sql,(total,))
#       self.conn.commit()