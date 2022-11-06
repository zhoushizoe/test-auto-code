"""
继承的概念
继承：
    复用父类的公开属性和方法
    拓展出新的属性和方法
继承的实现：
    语法：class 类名（父类列表）
    默认父类是object
    python支持多继承

"""
class Human:
    # 类属性
    message = "这是Human类的属性"

    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 实例方法

    def live(self):
        print("live in earth")


class Student(Human):
    def school(self):
        print("my school is 霍格沃滋")


stu = Student("ZOE", 18)
print(stu.name)
stu.school()
print(stu.age)
stu.live()
"""
类型检查：
isinstance（实例，类名）
    检查对象是否是某个类及其派生类的实例
issubclass（类名1，类名2）
    检查类名1是否是类名2的子类
"""
print(isinstance(stu, Human))
print(issubclass(Student, Human))
print(issubclass(Human, Student))