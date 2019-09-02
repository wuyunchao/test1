import requests
import json
from readConfig import ReadConfig
from tool.Logger import Log

log = Log()
readconfig = ReadConfig()

class PublicMethod(object):
    def __init__(self, method, url, data):
        self.method = method
        self.url = url
        self.data = data

    @property
    def headers(self):
        authorization = readconfig.get_headers('authorization')
        headers = {"Content-Type": 'application/json'}
        # 公司这边是通过鉴权参数来判断用户是否登录的
        headers['Authorization'] = authorization
        return headers

    def methodAPI(self):
        # 根据不同的访问方式来访问接口
        try:
            if self.method == 'post':
                res = requests.post(self.url, data=json.dumps(eval(self.data)), headers=self.headers)
                log.info("调用【 post 】方式")
            elif self.method == 'get':
                res = requests.get(self.url, params=self.data)
                log.info("调用【 get 】方式")
            return res
        except Exception as e:
            log.error('接口调用method不存在')
            log.error(str(e))

    def getStatusCode(self, res):
        # 获取返回信息status_code
        try:
            status_code = res.status_code
            log.info("获取返回信息status_code【" + str(status_code) + "】")
            return status_code
        except Exception as e:
            log.error('获取status_code失败')
            log.error(str(e))

    def getJson(self, res):
        try:
            json_data = res.json()
            log.info("成功获取接口返回信息json_data")
            return json_data
        except Exception as e:
            log.error('获取接口json_data失败')
            log.error(str(e))
    # 获取鉴权的值并存放到配置文件中
    def save_authorization(self):
        try:
            data = {"username": "xxx", "password": "xxx"}
            res = requests.post("https://baidu.com", data=data)
            authorization = res.json()['data']['jwt']
            readconfig.set_headers('authorization', authorization)
            log.info("成功存储参数到配置文件")
        except Exception as e:
            log.error('获取authorization失败')
            log.error(str(e))