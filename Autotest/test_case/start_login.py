from tool.readExcel import readExcel
from tool.common import PublicMethod
import unittest
import const
from readConfig import ReadConfig
from tool.Logger import Log
import HtmlTestRunner

read_config = ReadConfig()
log = Log()


class testLoginApi(unittest.TestCase):
    '''登录测试'''

    def setUp(self):
        self.file = read_config.get_test_file('test_file')
        self.URL_prefix = read_config.get_http("url")

    def test_login(self):

        '''测试登录接口'''
        # 获取excel内容
        test_File = const.TESTFILE  + self.file
        # test_File = r'C:\Users\吴运超\PycharmProjects\Autotest\test_Feil/'+self.file
        excel = readExcel(test_File)
        name = excel.getName
        data = excel.getData
        msg = excel.getMsg
        log.info(msg)
        url = excel.getUrl
        method = excel.getMethod
        id = excel.getId
        status_code = excel.getStatusCode
        # code = excel.getCode
        row = excel.getRows
        for i in range(0, row - 1):
            log.info("开始执行【{}】脚本".format(name[i]))
            api = PublicMethod(method[i], self.URL_prefix + url[i], data[i])
            # 存储鉴权值到配置文件
            # api.save_authorization()
            res = api.methodAPI()
            apistatus = api.getStatusCode(res)
            apijson = api.getJson(res)

            '''
             1. 验证返回的状态是否正确
             2. 验证Excel中msg的所有值是否都正确
             3. 这边判断msg是否为空，但是不做错误处理，因为有可能没有返回值的，所以就不判断
            '''
            # 判断返回的状态码是否正确
            self.assertEqual(apistatus, int(status_code[i]), msg='状态匹配不成功')
            log.info('{}.{}:状态测试成功'.format(id[i], name[i]))
            log.info(len(msg))

            # 验证Excel中msg的所有值是否都正确
            if len(msg) != 0:
                # excel取过来的msg转为字典格式
                dict_msg = eval(msg[i])


                # 循环遍历找到对应的key
                for key, value in dict_msg.items():
                    self.assertTrue(key in apijson.keys() or key in apijson['data'].keys())
                    response_msg = apijson[key] if key in apijson.keys() else apijson['data'][key]
                    if self.assertEqual(dict_msg[key], response_msg,
                                     msg='Excel获取的参数:[{0}]与返回的结果:[{1}]不一致,请检查;接口信息:{2}'
                                     .format(dict_msg[key],response_msg,apijson)) == None:
                        log.info('{}.{}:返回的字段[{}]验证OK'.format(id[i], name[i], key))
                    else :
                        print('12312312312')


                log.info("结束【{}】脚本测试".format(name[i]))
            else:
                log.info('没有需要验证的参数')
            log.info("*" * 30)

        log.info("测试结束")
        log.info("-" * 30)


if __name__ == '__main__':
    re = unittest.TestSuite()
    re.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(testLoginApi))
    with open('./report.html', 'w') as fp:
        runner = HtmlTestRunner.HTMLTestRunner(stream=fp,output=const.REPORTPATH, report_name='测试报告',report_title='测试',verbosity=2)
        runner.run(re)
