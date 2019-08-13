import pymysql
import noneValid


# dbConn.py
class ListTableInit:
    def __init__(self, host, port, user, password, db):
        params = {'host': host, 'port': port, 'user': user, 'password': password, 'db': db}
        print('listTableInit params: ', params)
        paramvalid = noneValid.DBConnValid(params)
        retmap = paramvalid.valid()
        print('valid res : ', retmap)
        if retmap.get('code') != 200:
            return retmap
        retmap = {'code': 200, 'message': '정상적으로 처리되었습니다.'}
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8')
        self.cursor = self.conn.cursor()
        return retmap

    def numcheck(self, param):
        sql = 'SELECT COUNT(1) FROM TARGET_LIST WHERE 1 = 1 and TARGET_SEQ = %s'
        self.cursor.execute(sql, param)
        row = self.cursor.fetchone()
        return row[0]

    def insert(self, param):
        print('param : ', param)
        sql = 'INSERT INTO TARGET_LIST (TARGET_SEQ, TARGET_SITE_TYPE, TARGET_CNTN_TYPE, TARGET_CNTN_URL, TARGET_TITLE, REG_ID, REG_DATE) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(sql, param)
        self.conn.commit()
        self.conn.close()

class CntnTableInit:
    def __init__(self, host, port, user, password, db):
        params = {'host': host, 'port': port, 'user': user, 'password': password, 'db': db}
        print('listTableInit params: ', params)
        paramvalid = noneValid.DBConnValid(params)
        retmap = paramvalid.valid()
        print('valid res : ', retmap)
        if retmap.get('code') != 200:
            return retmap
        retmap = {'code': 200, 'message': '정상적으로 처리되었습니다.'}
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8')
        self.cursor = self.conn.cursor()
        return retmap

    def getlistseq(self, param):
        sql = 'SELECT LIST_SEQ FROM TARGET_LIST WHERE 1 = 1 and TARGET_SEQ = %s'
        self.cursor.execute(sql, param)
        row = self.cursor.fetchone()
        return row[0]

    def insert(self, param):
        print('param : ', param)
        sql = 'INSERT INTO TARGET_CONTENTS (LIST_SEQ, TARGET_CNTN) VALUES (%s, %s)'
        self.cursor.execute(sql, param)
        self.conn.commit()
        self.conn.close()

