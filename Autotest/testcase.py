import get_properties
from tool import readExcel as exel
import unittest
import Api_request as request
import HtmlTestRunner

p = get_properties.Properties()
exel = exel.readExcel(r'C:\Users\吴运超\Documents\test.xlsx')



class Test(unittest.TestCase):


    def setUp(self):
        print("开始执行用例")

    def tearDown(self):
        print('执行用例结束')

    def test_moorelive(self):
        #设定所要读取对应数据的行数
        q = request.mooreliveTest(exel.getUrl, exel.getMethod, exel.getData)
        result = q.get_request()
        print(result)
        self.assertEqual(result['code'], 201,msg = '状态测试不成功')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test('test_moorelive'))
    fp = open('./reports/report.html','w',encoding='utf-8')
    runner = HtmlTestRunner.HTMLTestRunner(stream=fp,report_title='测试报告',report_name='测试')
    runner.run(suite)


