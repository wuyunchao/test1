


class Properties:
    def __init__(self,path ='hhaa.properties'):
        self.path = path

    def get_value(self,value):
        try:
            a = open(self.path, encoding='utf-8')
            re = {}
            for line in a.readlines():
                line = line.strip()
                if line.find('=')>1 and not line.startswith('#'):
                    tem = line.strip().replace(' ', '').split('=')
                    re[tem[0]] = tem[1]
            if value != None :
                return re[value]
            else:
                raise ValueError ('没有该元素')

        except Exception as err:
            print(err)
        else:
            a.close


#

# a = ['a','b']
# b = {}
# print(a[0])
# b['aa']= 'bb'
# print(b)
#
#
# a = ('a','b','c')
# q,w,e = a
# print(e)
