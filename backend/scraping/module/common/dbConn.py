import pymysql


# dbConn.py
class init:
    def __init__(self, host, port, user, password, db):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8')
        self.cursor = self.conn.cursor()

    def gallnum_check(self, param):
        sql = 'SELECT COUNT(1) FROM TARGET_LIST WHERE 1 = 1 and TARGET_SEQ = %s'
        self.cursor.execute(sql, param)
        row = self.cursor.fetchone()
        self.conn.close()
        return row[0]

    def insert_list(self, param):
        sql = 'INSERT INTO TARGET_LIST (TARGET_SEQ, TARGET_SITE_TYPE, TARGET_CNTN_TYPE, TARGET_CNTN_URL, TARGET_TITLE, REG_ID, REG_DATE) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(sql, param)
        self.conn.commit()
        self.conn.close()


