"""
使用 raise 手动触发异常
try

except

else

finally
"""

try:
    int('db')
except ValueError as Be:
    print(Be)
except BaseException as BB:
    print(BB)
else:
    print('没有发生异常才会执行的代码')
finally:
    print('不管发布发生都会执行夫的异常')
