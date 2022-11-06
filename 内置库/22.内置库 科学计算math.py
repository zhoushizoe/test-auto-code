"""
math函数
math函数，python提供的内置数学类函数库，包含了很多数学公式。
比如：幂函数运算，三角函数，高等函数运算等
    数字常数
    数论与表示函数
    幂对数函数
    三角对数函数
    高等特殊函数
"""
"""
数字常量：
    math.pi:圆周率
    math.e:自然对数，值为2.7182818....
    math.inf:∞正无穷大
    -math.inf:负无穷大
    math.nan:NAN,非数字NAN(Not a Number)
"""
import math

print(math.pi)
print(math.e)
print(math.inf)
print(-math.inf)
print(math.nan)
"""
数论与表示函数：具体可以查询math库
"""
# 向上取整 >4.3的最小的整数   5
print(math.ceil(4.3))
# 向上取整 >-4.3的最小的整数   -4
print(math.ceil(-4.3))
# 向下取整
print(math.floor(5.1))
"""
幂函数和对数函数（未一一列举）
"""
# 返回x的y次幂，
print(math.pow(3, 2))  # 3的2次幂
# 返回e的x次幂，e是自然对数
print(math.exp(3))  # e的三次幂
# 返回x的平方根
print(math.sqrt(9))  # 9的平方根
"""
三角函数，高等特殊函数
"""
"""
实战练习：
常量、数论与表示函数、幂函数与对数函数
一天365天，以第一天的能力值为基数，记为1.0,
当努力学习时，能力值相比前一天提高1%
当没有学习时能力值相比前一天下降1%
每天努力和每天放任，一年下来的能力值相差多少呢？
"""
day = 1
able_value = 1.0
# while day < 101:
#     add_able_value = able_value * 0.01
#     able_value = able_value+add_able_value
#     day += 1
#     print(able_value)
while day <100:
    subtract_able_value = able_value * 0.01
    able_value = able_value - subtract_able_value
    day += 1
    print(able_value)