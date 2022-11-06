"""
闭包函数
    闭包的内部函数中，对外部作用域的变量进行引用
    闭包无法修改外部函数的局部变量
    闭包可以保存当前的运行环境
"""


# def garde_student(garde):
#     def inner(name, gender):
#         print(f"恭喜你开学了，\
#         你的姓名是：{name},\
#         你的性别是{gender}，\
#         你的年级是{garde},快去报道把")
#     return inner
#
#
# student = garde_student(1)
# student("zoe", "girl")
# student("zhou", "men")
import datetime

"""
装饰器：
行业需求：涉及python技术栈
使用需求：优化代码的可读性，可维护性
"""
"""函数在开始执行和结束执行的时候分别打印提示信息"""


# def start():
#     print("this is a def")
#
#
# print("函数开始执行")
# start()
# print("函数结束执行")

# def start():
#     print("this is a def")
#
#
# def function_tips():
#     print("start")
#     start()
#     print("end")
#
#
# function_tips()

# def start():
#     print("this is first start" )
#
#
# def start2():
#     print("this is first start2")
#
#
# def function(func):
#     print("def is start")
#     func()
#     print("def is end")


# function(start2)


# def timer(func):
#     def inner():
#         print("this is start one")
#         func()
#         print("this is end two")
#     return inner
#
#
# def student():
#     print("this is the func three")
#
#
# timer(student)

"""
学习使用装饰器
    第一步：定义两个函数，一个内函数，一个外函数
    第二步：在内函数添加装饰器的逻辑
    第三步：把内函数的函数对象return出去
    第四步：装饰器的使用
    第五步：在装饰器执行过程中，会自动传入一个参数，参数就是被装饰器函数的函数对象
    第六部：添加被装饰函数的执行步骤
"""


# def out_study(func):
#     def inner_study():
#         print("内函数的装饰器使用开始")
#         func()
#         print("内函数的装饰器使用结束")
#     return inner_study
#
#
# @out_study
# def study_1():
#     print("学习使用装饰器")
#
#
# study_1()
"""
装饰器的练习
    实现一个计时器的装饰器，计算函数执行时间
"""

#
# def timer(func):
#     def inner():
#         start_time = datetime.datetime.now()
#         func()
#         end_time = datetime.datetime.now()
#         ing_time = end_time - start_time
#         print(f"函数运行的时间为{ing_time}")
#
#     return inner
#
#
# @timer
# def pratice():
#     print("实现一个计时器的装饰器，计算函数执行时间")
#
#
# # pratice()
# @timer
# def pratice_2():
#     print("123")
#
#
# pratice_2()

"""
如果被装饰函数有行参，需要在内函数加行参，在函数参数调用的时候添加参数信息
如果写死一个函数，但是无法确定被装饰函数的参数数量，会报错
解决方案：将两个地方的参数换成不定长参数
"""


def timer(func):
    def inner(*args, **kwargs):  # 添加不定长参数
        start_time = datetime.datetime.now()
        func(*args, **kwargs)  # 添加不定长参数
        end_time = datetime.datetime.now()
        ing_time = end_time - start_time
        print(f"函数运行的时间为{ing_time}")

    return inner
@timer
def pratice(name, age, sex):
    print(f"实现一个计时器的装饰器，计算函数执行时间:姓名是{name}")


pratice("zoe", "18", "girl")
