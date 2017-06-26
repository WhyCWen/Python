"""
file 处理的Demo
1,打开一个file 使用open
2,读/写
3,close 关闭文件
"""
#1 打开一个文件 以写入的模式 如果文件不存在则创建一个文件
#有可能会发生中文乱码 指定编码方式
files = open('recordOne.txt','r+',encoding='utf-8')
#写入文本
files.write("你是一个小婊砸")
#3,关闭文件
print(files.readlines())
files.close()

"""

"""

class MyException(Exception):
    pass

try:
    i=0
    j=0
    while i < 10:
        j = 0
        while j < 10:
            j += 1
            if i==3:
                raise  MyException
            print(i+j)
        i += 1
except MyException:
    pass

while True:
    s = input("please input something: ")

    with open('apendText.txt','a+',encoding='utf-8') as f:
        if s in ['exit', 'quit']:
            with open('apendText.txt', 'r', encoding='utf-8') as fr:
                for o in fr:
                    print(o)
                fr.close()
            f.close()
            break
        f.write(s+'\n')

