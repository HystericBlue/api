import pymysql


# dbconfig.py
class DBController:
    def __init__(self, host, port, user, password, db):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8')
        self.cursor = self.conn.cursor()

    def select_list_count(self):
        sql = 'SELECT COUNT(1) FROM TARGET_LIST WHERE 1 = 1'
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        self.conn.close()
        return row

    def insert_list(self, param):
        print('parma : ', param)
        sql = 'INSERT INTO TARGET_LIST (TARGET_SEQ, TARGET_SITE_TYPE, TARGET_CNTN_TYPE, TARGET_CNTN_URL, TARGET_TITLE, REG_ID, REG_DATE) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(sql, param)
        self.conn.commit()
        self.conn.close()


