"""
匿名函数
没有名字的函数，用lambda表达式创建匿名函数
使用场景：
需要一个函数，但是又不想费神去命名这个函数
通常在这个函数只使用一次的场景下
可以指定短小的回调函数
"""
"""
匿名函数语法：
result：调用lambdab表达式
[arg1[,arg2...argn]]:可选，指定要传递的参数列表
expression：必选，指定一个实现具体功能的表达式
"""
import math
#   得到圆的面积
def circus_1(r):
    result2 = math.pi *r**2
    return result2
r = 10
print(f"圆的半径为{r},圆的面积为{circus_1(r)}")
#   lambda 表达式不可以省略前边的变量
result = lambda r : math.pi*r*r
r = 3
print(f"圆的半径为{r},圆的面积为{result(r)}")

#   对获取到的信息进行排序
book_info = [
    ("第一本书",20),
    ("第二本书",25),
    ("第三本书",10)
]
#lambda x:x[1]返回了每个元组中的第二个元素
book_info.sort(key=lambda x:x[1])
# print(book_info)
# for i in range(1,10):
#     for y in range(1,i+1):
#         print(f"{i}*{y}={i*y}",end=' ')
#     print("\r")
# j=1
# while j <= 9:
#     for k in range(1,j+1):
#         print(f"{k}*{j}={j*k}",end=' ')
#     print("\r")
#     j+=1
# for x in range(1,10):
#     for y in range(1,x+1):
#         print(f"{y}*{x}={x*y}",end = " ")
#     print("\r")