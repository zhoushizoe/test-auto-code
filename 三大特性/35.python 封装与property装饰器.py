"""
封装
    隐藏：属性和实现细节，不允许外部直接访问
    暴露：公开方法，实现对内部信息的操作和访问
封装的作用
    限制安全的访问和操作，提高数据的安全性
    可进行数据检查，从而有利于保证对象信息的完整性
封装的实现：隐藏
    保护属性：_属性名
    私有属性：__属性名
        被视作：_类名__属性名
"""
# 定义一个类


# class Acccount:
#     # 普通账户：
#     bank = "BOC"
#     # 保护属性（内部属性）
#     _username = "zoe"
#     # 私有属性
#     __password = "8888"
# print(Acccount.bank)
# print(Acccount._username)
# # 私有属性，不能被调用
# print(Acccount._Acccount__password)
# print(Acccount.__dict__)
"""
封装的实现：暴露
提供数据访问功能（getter）
    计算属性
    语法：使用@property装饰器
    调用：实例.方法名
"""


# class Account:
#     # 普通账户：
#     bank = "BOC"
#     # 保护属性（内部属性）
#     _username = "zoe"
#     # 私有属性
#     __password = "8888"
#
#     # 添加@property装饰器，提供数据访问功能
#     @property
#     def password(self):
#         return self.__password
#     # 修改私有属性，提供数据操作功能（setter）；语法：使用@计算属性名.setter装饰器；调用：实例.方法名
#     @password.setter
#     def password(self, value):
#         if len(value) >= 8:
#             self.__password = value
#         else:
#             print("密码的长度最少要有八位")
#
#
# # 实例化对象
# obj = Account()
# # 打印出私有属性
# # print(obj.password)
# # 修改私有属性
# # obj.password = "zoeisagoodgile"
# # print(obj.password)
# obj.password = "123"
# print(obj.password)
class Account:
    bank = "OBC"
    _username = "zoe"
    __password = "zxp"
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, value):
        if len(value) >= 8:
            self.__password = value
        else:
            print("密码的长度为8位")
obj = Account()
print(obj.bank)
print(obj._username)
# print(obj.password)
obj.password = "123456"
print(obj.password)

