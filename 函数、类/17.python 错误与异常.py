"""
语法错误与定位
异常捕获、异常处理
自定义异常
"""
"""
错误：
    语法错误:syntaeerror:少一个if后边的冒号之类的
    逻辑错误：语法没有错误，编写的逻辑有问题
    系统错误：
异常：
   程序执行过程中出现的未知错误
   语法和逻辑都是正确的
   程序业务逻辑不完善引起的程序漏洞 

错误和异常的区别：
    异常可以捕获和处理
    错误一般是编码错误，逻辑错误，系统错误
"""
"""
    常见的异常类型：
        除零异常、名称异常、索引异常、键异常、值异常、属性异常等等
"""
# 除零异常:ZeroDivisionError
# a = 1
# b = 0
# print(a / b)
# 名称异常:NameError
# num = 1
# if num > 1:
#     print(f"{num}")
# elif nume < 2:
#     print(f"{num+1}")
# 索引异常：IndexError
# list1 = [1, 2, 3, 4]
# print(list1[5])
# 键异常：KeyError
# dict1 = {1: 2, 3: 4, 5: 6}
# print(dict1[7])
# 值异常：ValueError
# num2 = "abc"
# print(int(num2))
# 属性异常


def div(a, b):
    return a / b


try:
    print(div(1, 0))
except Exception as e:
    print(e)
    print("除数不能为0")

f = open("16.python 模块与包.py")
# f.read()
# f.close()
# try里编写的是执行代码；except里放置的是发生异常时执行的代码
try:
    f.read()
    print("正常打开")

except Exception :
    f.close()
    print("抛出一个异常")
finally:# 最终都会被执行，无论有异常还是没异常
    print("最后都会被执行")
"""
try:
    执行代码
except:
    发生异常时执行的代码
else：
    没有异常时执行的代码
finally:
    最后都会执行的代码块
"""


def set_age(name, num):
    if num <= 0 or num >200:
        raise ValueError# 主动抛出了一个异常，使用raise
    else:
        print(f"{name}的年龄是{num}岁")


set_age("zoe",  0)

"""
自定义异常
class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
"""

"""
异常/错误处理流程
检测到错误——引发异常——捕获异常操作
"""





