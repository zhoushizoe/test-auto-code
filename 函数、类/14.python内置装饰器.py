"""
内置类装饰器：不用实例化、直接调用；提升代码的可读行
@classmethod：类方法
@staticmethod：静态方法
"""
#   普通方法


class nomal:
    #   类变量
    para = 0

    def method(self, mood):
        print("这是一个普通方法", self.para)
#   实例化


nomal_way = nomal()
#   实例化后调用方法
nomal_way.method("happy")
nomal_two = nomal()
nomal_two.method("down")

"""
类方法：
定义，使用@classmethod装饰器，第一个参数为类本身，所以通常使用cls命名做区分
调用：无序实例化，直接通过类.方法名调用
"""
class method_1():
    @classmethod
    def class_2(cls):    #类方法内，不可以直接调用实例方法，实例变量
        print("this is a class method")
    #   调用过程中，类和实例都可以直接调用类方法


method_1.class_2()


class Test:
    class_4 = 0

    @classmethod
    def method_2(cls):
        print(Test.class_4)


Test.method_2()
# 练习一个普通方法


class nomal_1():
    def test_nomal(self,one,two):
        print(f"一定要传入两个参数：{one},{two}")


one_test = nomal_1()
one_test.test_nomal(1, 2)

"""
静态方法：
定义：
    使用@staticmethod装饰器，没有和类本身有关的参数；无法直接使用任何类变量，类方法或者实例方法，实例变量
调用：
    无需实例化，直接通过类.方法名调用，也可以通过实例.方法名调用
"""


class clame_1():
    #使用staticmethod装饰器；没有self或者cls
    @staticmethod
    def method_1():
        print("this is a staticmethod")


clame_1.method_1()
"""
实际案例：下边的代码实现的需求是格式化输出时间；
        如果现在需求变更，输入年月日没法保证格式统一，可能是json，可能是其他格式的字符串
        在不修改构造函数的前提下，如何更改代码
"""
#定义一个类


# class DateFormat:
#     # 构造方法
#     def __init__(self, year=0, month=0, day=0):
#         # 使用self绑定给自身
#         self.year = year
#         self.month = month
#         self.day = day
#
#     def out_date(self):
#         return f"输入的时间为{self.year},{self.month},{self.day}"
#         # 构造普通函数
#
#
# def json_format(json_data):
#     year, month, day = json_data["year"], json_data["month"], json_data["day"]
#     # print(year, month, day)
#     return year, month, day
#     # return
#
#
# # print(json_format({"year": 2021, "month": 3, "day": 23}))
#
# year, month, day = json_format({"year": 2021, "month": 3, "day": 23})
# demo = DateFormat(year, month, day)
# print(demo.out_date())


# class TimeOne:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def out_human(self):
#         return f"这个人的名字叫{self.name},年龄是{self.age},她是一个{self.sex}"
#
#
# def woman(info):
#     name, age, sex = info["name"], info["age"], info["sex"]
#     return name, age, sex
#
#
# woman({"name": "anna", "age": 18, "sex": "man"})
#
# name, age, sex = woman({"name": "anna", "age": 18, "sex": "man"})
# zoe = TimeOne(name, age, sex)
# print(zoe.out_human())

# class HumanTow:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def human_info(self):
#         return f"这个人的名字是{self.name},这个人的年龄是{self.age},这个人是个{self.sex}"
#
#
# """
# 现在有格式为字典的数据需要转化成标准格式，字典为：{"name":"zoe","age":18","sex":"girl"}
# """
#
#
# def zoe_one(info):
#     name, age, sex = info["name"], info["age"], info["sex"]
#     return name, age, sex
#
#
# zoe_one({"name": "zoe", "age": 18, "sex": "girl"})
# name, age, sex = zoe_one({"name": "zoe", "age": 18, "sex": "girl"})
# zoe = HumanTow(name, age, sex)
# print(zoe.human_info())


class DateFormat:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def out_date(self):
        return f"输入的时间为{self.year}年，{self.month}月，{self.day}日"

    @classmethod
    def json_format(cls, json_data):
        year, month, day = json_data["year"], json_data["month"], json_data["day"]
        return cls(year, month, day)


json_data = {"year": 2011, "month": 10, "day": 26}
demo = DateFormat.json_format(json_data)
print(demo.out_date())

"""
静态方法实际案例
"""
class Game:
    def __init__(self, first_hero, second_hero):
        self.first_hero = first_hero
        self.second_hero = second_hero

    # pk由和实例变量交互的部分，所以需要定义为一个普通方法
    def pk(self):
        print(f"这场比赛由{self.first_hero} pk {self.second_hero}")

# 游戏开始没有和类或者实例交互的地方，可以使用staticmethod
    @staticmethod
    def start():
        print("游戏开始")


Game.start()
game_1 = Game("ZOE", "GAMA")
game_1.pk()







