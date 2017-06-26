class SelfInstance(object):

    def __int__(self,a,b):
        self._a = a
        self.b = b

    #包装成成员变量 si = SelfInstance(),si.a 来获取变量值
    @property
    def a(self):
        return self._a
    def info(self):
        self.set_a(10)
        self.set_b(20)
        print('a:',self._a,"bL",self.b)

    def set_a(self,a):
        self._a = a
    def set_b(self,b):
        self.b =b
    def get_a(self):
        return self._a
    def get_b(self):
        return  self.b
if __name__ == '__main__':
    si = SelfInstance()
    si.info()
    #使用 @property 来装饰成成员变量
    print(si.a)
    print(si.get_b())