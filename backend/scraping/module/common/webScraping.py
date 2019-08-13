import requests

# webScraping.py
class init:
    """
    headers : (dict) url
    """
    def __init__(self, headers):
        if len(headers) == 0:
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
            }
        if headers.get('User-Agent') is None and headers.get('Accept') is None:
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
            }
        else:
            self.headers = headers
        print('headers : ', self.headers)

    """
    arglist[0] : (str) url
    arglist[1] : (str) method
    arglist[2] : (dict) params 
    :returns code, meesage, data
    """
    def targetsite(self, *arglist):
        if not arglist:
            retmap = {'code': 404, 'message': 'Not argument'}
            return retmap
        if len(arglist) == 1:
            retmap = {'code': 404, 'message': 'Not method'}
            return retmap
        elif len(arglist) == 2:
            url = arglist[0]
            method = arglist[1]
            params = {}
        elif len(arglist) == 3:
            url = arglist[0]
            method = arglist[1]
            if type(arglist[2]) == dict:
                params = arglist[2]
            else:
                params = {}
        else:
            retmap = {'code': 500, 'message': 'argument 수가 초과되었습니다.'}
            return retmap
        if method == 'post':
            res = requests.post(url, headers=self.headers, data=params)
        elif method == 'put':
            res = requests.put(url, headers=self.headers, data=params)
        elif method == 'delete':
            res = requests.delete(url, headers=self.headers, data=params)
        else:
            res = requests.get(url, headers=self.headers, data=params)
        retmap = {'code': res.status_code, 'message': '성공하였습니다.', 'data': res.text}
        return retmap