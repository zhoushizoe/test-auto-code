#   tuple 元组
"""
元组定义：
元组是有序的不可变对象集合
元组使用小括号包括，各个对象之间使用逗号分割
元组是异构的，可以包含多种数据类型

"""
"""
元组使用：创建
使用逗号分隔
通过小括号填充元素
通过构造方法tuple（iterable）
"""
#   使用逗号分隔创建元组
tup1 = 1,2,3,4,5
print(type(tup1),tup1)
#   通过小括号填充元素
tup2 = (1,2,3,4,6)
print(type(tup2),tup2)
#   通过构造函数tuple（iterable）构造元组
tup3 = ()
print(type(tup3),tup3)
tup4 = tuple("hello,world")
print(type(tup4),tup4)
tup5 = tuple([1,2,3,4,5])
print(type(tup5),tup5)
#   单元素元组，逗号不可或缺
tup6= (1,)
print(tup6)
"""
元组索引：
可以通过索引值来访问对应的元素
正向索引：默认值从0开始
反向索引，默认值从-1开始
"""
tup7 = (1,2,3,4,5)
print(tup7[3])
print(tup7[-2])
"""
切片[start:stop:step]
三个值都是可选的，非必填
start值：指示开始索引值，如果没有指定，默认开始值为0
stop值：指示到哪个索引值结束，但不包括这个结束的索引值。如果没有指定，则取列表允许的最大索引值
step值：步长值指示每一步大小，如果没有指定，则默认步长值为1
"""
tup8 = (0,1,2,3,4,5,6,7,8,9,0)
print(tup8[2::])
print(tup8[1:10:2])
print(tup8[::2])
print(tup8[:7:])
print(tup8[::-1])
"""
元组不可变，不支持新增，删除，修改等操作
元组常用方法
index（）
count（）
"""
"""
index（item）
返回与目标元素相匹配的首个元素的索引
目标必须在元组中存在，否则会报错
"""
tup9 = ("nihao","yes","allright")
print(tup9.index("nihao"))
print(tup9)
tup10 = tuple("what the matter")
print(tup10)
print(tup10.index("h"))

"""
count(item):返回某个元素出现的次数
入参：对象item
返回：次数
"""
tup11 = tuple("tupleisverygoodthingT")
#   "t"在tup11中出现了两次，返回值为2
print(tup11.count("t"))
#   "a"在tup11中没有，返回0
print(tup11.count("a"))

"""
元组解包
元组解包：把一个可迭代对象里的元素，一并赋值到由对应的变量组成的元组中 
前提：两边的元素个数是相同的
"""
#   传统逐个赋值的方式
tup12 = 1,2,3
a = tup12[0]
b = tup12[1]
c = tup12[2]
print(a,b,c)
#   解包平行赋值
d,e,f = (4,5,6)
print(d,e,f)
"""
元组与列表
相同点：
    都是有序的
    都是异构的， 能够包含不同类型的对象
    都支持索引和切片
区别
    声明方式不同，元组使用（），列表使用[]
    列表是可变的，元组是不可变的
"""
