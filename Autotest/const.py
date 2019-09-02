# coding:utf-8
import sys, os


class _const:
    '''全局路径
    @:var CONFPATH:config文件地址
    @:key CASEFILEPATH:测试用例路径
    @:key REPORTPATH :测试报告路径地址
    '''


    class ConstError(TypeError): pass


    class ConstCaseError(ConstError): pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("can't change const %s" % name)
        if not name.isupper():
            raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
        self.__dict__[name] = value


sys.modules[__name__] = _const()

'''全局路径= 当前文件的父目录 + 目录'''

_const.CONFPATH = os.path.dirname(__file__) + '/config.ini'

_const.CASEFILEPATH = os.path.dirname(__file__) + "/test_case/"

_const.REPORTPATH = os.path.dirname(__file__) + "/reports/"

_const.LOGPATH = os.path.dirname(__file__) + '/LOG/'

_const.TESTFILE = os.path.dirname(__file__) + '/test_Feil/'

