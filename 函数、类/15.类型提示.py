"""
类型提示的好处：
1.增强代码的可读性
2.ide中代码提示
3.静态代码检查
"""


# name:str,为参数指定数据类型，->:为返回的参数指定数据类型
def tips(name: str) -> str:
    print(name)


tips("zhangsan")


# IDE中的提示功能
def tips(name: str) -> str:
    print(name)


from typing import List
# 类型别名
# 列表类型的，每一个数据类型都是float
Vector = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


print(scale(1.1, [2, 3, 5]))


#  自定义类型
class Student:
    name: str
    age: int


def get_stu(name: str) -> Student:
    return Student()


get_stu("zoe")
# 安装mypy：pip install mypy
# 运行mypy：mypy demo.py
a: List[int] = []
a = [1, 2, "a"]
