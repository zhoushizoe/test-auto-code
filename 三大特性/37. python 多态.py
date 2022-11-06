"""
多态（Polymorphism）：
    多态的概念
        同名方法呈现多种行为
    多态的表现
        +号
            加法：数字+数字
            拼接：字符串+字符串
            合并：列表+列表
        len（）函数
            可以接收字符串
            可以接收列表
        同名变量调用同名方法呈现多种行为
    多态与继承
"""
# 多态的表现+号
print(1+1)
print("nihao"+" my boy")
print([1, 2, 3]+[4, 5, 6])
# 多态的表现len（）
a = "123456"
print(len(a))
b = [1, 2, 3, 4, 5, 6]
print(len(b))
# 多态的表现：同名变量调用同名方法呈现多种行为


class China:
    def speak(self):
        print("汉语")


class Usa:
    def speak(self):
        print("english")


zoe = China()
BOB = Usa()
for x in (zoe, BOB):
    x.speak()
"""
多态与继承
    方法重写（override）：子类的方法名称与父类相同
    重写构造方法：
        super().__init__()
        父类名.__init__(self)
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
    def __init__(self, name, age, school):
        # 访问父类的构造方法
        super().__init__(name, age)
        # super（Student，self).__init__(name, age)
        # Human.__init__(self, name, age)
        # 子类实例属性（个性）
        self.school = school
    # 重写普通的方法：

    def live(self):
        print(f"{self.school}")


stu = Student("ZOE", 18, "霍格沃滋")
print(stu.name)
print(stu.school)
print(stu.age)
stu.live()


