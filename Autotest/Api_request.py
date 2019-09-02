import requests
import json


class mooreliveTest():

    def __init__(self, url, method, parameter, headers=None):
        self.url = url
        self.method = method
        self.parameter = parameter
        self.headers = headers

    def get_request(self):

        if self.method == 'get' or self.method == 'GET':
            try:
                r = requests.get(self.url, params=self.parameter, headers=self.headers)
                return r.json()
            except Exception as err:
                print('GET请求失败:', err)
        elif self.method == 'post' or self.method == 'POST':
            try:
             r = requests.post(self.url, json=self.parameter, headers=self.headers)

             return r.json()
            except Exception as err:
                print('POST请求失败:', err)
        else:
            print("请求方法错误")


if __name__ == '__main__':
    m = mooreliveTest('https://moore.live/news/api/list/1/', 'post1', 'page=1&per_page=10&recommend=true\
')
    print(m.get_request())
