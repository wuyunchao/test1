import xlrd


class readExcel(object):
    def __init__(self, path):
        self.path = path

    @property
    def getSheet(self):
        # 获取索引
        xl = xlrd.open_workbook(self.path)
        sheet = xl.sheet_by_index(0)
        # print( xl.sheet_names() )   打印所有sheet名字
        # print (sheet.cell_value( 2, 3 ))   打印第3行第4列
        return sheet

    @property
    def getRows(self):
        # 获取行数
        row = self.getSheet.nrows
        return row

    @property
    def getCol(self):
        # 获取列数
        col = self.getSheet.ncols
        return col

    # 以下是分别获取每一列的数值

    @property
    def getId(self):
        TestId = []
        for i in range( 1, self.getRows ):
            TestId.append( self.getSheet.cell_value( i, 0 ) )
        print(TestId)
        return TestId

    @property
    def getName(self):
        TestName = []
        for i in range(1, self.getRows):
            TestName.append(self.getSheet.cell_value(i, 1))
        print(TestName)
        return TestName

    @property
    def getUrl(self):
        TestUrl = []
        for i in range(1, self.getRows):
            TestUrl.append(self.getSheet.cell_value(i, 2))
        return TestUrl

    @property
    def getMethod(self):
        TestMethod = []
        for i in range(1, self.getRows):
            TestMethod.append(self.getSheet.cell_value(i, 3))
        return TestMethod

    @property
    def getData(self):
        TestData = []
        for i in range(1, self.getRows):
            TestData.append(self.getSheet.cell_value(i, 4))
        return TestData

    @property
    def getStatusCode(self):
        TestUid = []
        for i in range(1, self.getRows):
            TestUid.append(self.getSheet.cell_value(i, 5))
        return TestUid

    # @property
    # def getCode(self):
    #     TestCode = []
    #     for i in range(1, self.getRows):
    #         TestCode.append(self.getSheet.cell_value(i, 6))
    #     return TestCode

    @property
    def getMsg(self):
        test_msg = []
        for i in range(1, self.getRows):
            test_msg.append(self.getSheet.cell_value(i, 6))
        return test_msg


if __name__ == '__main__':
    e = readExcel(r'C:\Users\吴运超\PycharmProjects\Autotest\test_Feil\test.xlsx').getMsg

    print(e)
