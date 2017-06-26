"""
python 的函数的使用
    使用 def 来定义函数

"""

def testOne():
    i = 9
    j = 8
    return i+j

print(testOne())

# 有参数的使用
def testTwoP(name ="xiaoming"):
    print("I am ",name)

#没有使用返回值 返回的是 none
print(testTwoP())

#可变参数 *args 是一个元组类型的数据 tuple

def testThree(name = "完美",age = 12, *args):
    print(name,age)
    print(args)
testThree("dg",1,12,3)