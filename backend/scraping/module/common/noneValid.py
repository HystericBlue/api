# noneValid.py

class DBConnValid:
    def __init__(self, params={}):
        self.params = params

    def valid(self):
        if type(self.params) != dict:
            retmap = {'code': 500, 'message': 'dict 타입이 아닙니다.'}
            return retmap
        keys = self.params.keys()
        objchecked = True
        for key in keys:
            object = self.params.get(key)
            if object == '' or object is None:
                objchecked = False
                retmap = {'code': 404, 'message': key+' 가 없습니다.'}
                return retmap
            if objchecked == False:
                break
        retmap = {'code': 200, 'message': '정상적으로 처리되었습니다.'}
        return retmap