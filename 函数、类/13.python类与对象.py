"""
面向对象：
在编程的时候尽可能的去模拟真实的现实世界，按照现实世界中的逻辑去处理问题，分析问题中参与其中的有哪些实体
这些实体应该有什么属性和方法，我们如何通过调用这些实体的属性和方法去解决问题/
面向过程
    一种以过程为中心的编程思想
    首先分析解决问题所需要的步骤
    然后用函数将这些步骤一步步的实现
    最后按顺序依次调用运行
面向对象
    是一种更符合我们人类思维习惯的编程思想
    面向对象开发就是不断的创建对象，使用对象，操作对象做事情
    可以将复杂的事情简单化
"""
"""
类（class）：用来描述具有相同的属性和方法的对象的集合。它定义了集合中每个对象所共有的属性和方法
对象（object）：也称为类的实例，是一个具体存在的实体
"""
"""
类的定义：
class关键字：
    class类名（父类名）:
    """"类的帮助信息（三个引号）""""
    属性
    方法
"""
#   类的声明
class Human(object):
    """人类"""
    #   定义属性（类属性）
    message = "这是类属性"
#   通过类名访问类属性
print(Human.message)

"""
类的方法：
    实例方法：构造方法
    类方法：静态方法
"""
"""
构造方法与实例化
    作用：实例化对象
    语法：def__init__(self,参数列表)
    访问：类名（参数列表）
"""
#   先构造一个类
class Woman:
    #   定义属性
    message = "this is calss attribute"
    #   定义构造方法
    def __init__ (self,name,age):
        #   实例属性（变量），使用self绑定给自身
        self.name = name
        self.age = age
        print("这是构造方法")


#   实例化方法
#   实例化对象
person = Woman("zoe", 12)

#   通过实例访问类属性
print(person.message)

#   通过实例访问实例属性
print(person.name)
print(person.age)

"""
常规的实例方法
作用：提供每个类的实例共享的方法
语法：def 方法名（self,参数列表）
访问：实例.方法名（参数列表）
方法体和函数的区别：函数实现的是某个独立的功能；而实例方法是实现类中的行为，属于类的部分
实例方法主要用于定义类的对象、行为，功能实现
"""
#   形参：self
class people:
    def learn(self,course):
        print((f"正在学习：{course}"))
study = people()
study.learn("english,math")
"""
self：类体中第一个参数总是指向调用该方法的对象；在构造方法中，引用该构造方法中正在初始化的对象；
        在普通实例中：引用调用该方法的对象
self最大的作用：引用当前方法的调用者
"""
class school:
    def leason_1 (self,course,time,teacher):
        print(f"i am learning {course},{time} a week,{teacher} is my teacher")
#   实例化
study_1 = school()
#通过实例访问实例方法
study_1.leason_1("english","three times","zoe")

"""
类方法：
    作用：可以操作类的详细信息
    语法：@classmethod
    访问：类名.类方法名（参数列表）
"""
class Learn_1:
    #一个类属性
    times = 0
    #   定义一个类方法
    @classmethod
    def time(cls):
        print("我创建了一个类方法")
        cls.times += 2
#通过类名访问类方法
Learn_1.time()
print(Learn_1.times)

"""
静态方法：
@staticmethod
静态方法，其实就是我们学过的函数
和函数唯一的区别是：静态方法定义在类这个空间（类命名空间）中
而函数则定义在程序所在的空间（全局命名空间）中。

静态方法没有类似 self、cls 这样的特殊参数
因此 Python 解释器不会对它包含的参数做任何类或对象的绑定。
也正因为如此，类的静态方法中无法调用任何类属性和类方法。
"""


#   静态方法
class Quiet:
    #   静态方法，声明之后不会绑定到self
    @staticmethod
    def book():
        print("reding a book")


Quiet.book()


class Test_2:
    def Text_1(self,name,age):
        self.name = name
        self.age = age
        print(f"{name},{age}")



class Woman2:
    #   定义属性
    message = "this is calss attribute"
    #   定义构造方法
    def __init__ (self,name,age):
        #   实例属性（变量），使用self绑定给自身
        self.name = name
        self.age = age
        print("这是构造方法")

    def fun(self):
        self.date = 10



t = Test_2()

t.Text_1("zhangsan",18)
t.Text_1("zhangsan",23)

w = Woman2()
print(w.name)
