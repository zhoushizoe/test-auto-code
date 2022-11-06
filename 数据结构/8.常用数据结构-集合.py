"""set 集合"""
"""
集合定义
无序的唯一对象集合
用大括号{}包围，对象相互之间使用逗号分隔
集合是动态的，可以随时添加或删除元素
集合是异构的，可以包含不同类型的数据
"""
"""
集合使用：创建
    使用{}填充元素
    通过构造方法set（）
    通过集合推导式
"""
#   使用{}填充元素
set1 = {1,2,3}
print(type(set1),set1)
#   创建空的集合时不能使用{}
#   通过构造方法set（）
#   set可接受一个可迭代的对象作为参数
#       可迭代对象：可以使用for循环遍历其中元素的一个对象
#       比如：字符串、列表，元组、集合、字典
#字符串构造集合
set2 = set("nihao")
print(type(set2),set2)
#列表构造集合
set3 =set (["hi","nihao"])
print(type(set3),set3)
#集合构造集合
set4 = set((1,2,3,4))
print(set4)
#创造空的集合对象
set5 = set()
print(type(set5),set5)
#   集合推导式
set6 = {i for i in range(1,11) if i % 2 ==0}
print(set6)
"""
集合使用：成员检测
in：判断元素是否在集合中存在
not in：判断元素是否在集合中不存在
"""
set7 = {1,2,3,4,5,6}
print(9 in set7)
print(2 in set7)
print(3 not in set7)
print(9 not in set7)
"""
集合方法
add()
update()
remove()
discard()
pop()
clear()
"""
#   add(item):将单个对象添加到集合中
set8 = {1}
set8.add(2)
print(set8)
#   update（iterable），批量添加来自可迭代对象中的所有元素；入参：可迭代对象iterable，返回：None
set9 = set()
set10 = {1,2}
set9.update("abcdefg")
set9.update(set10)
print(set9)
#   remove(item)：从集合中移除指定元素item，元素不存在时会报错:KeyError
set11 = {"weather",2,4,"a","a",5}
#移除set11中的"a"元素
set11.remove("a")
print(set11)
#移除一个不存在set11中的元素，会报错
#set11.remove("b")
#print(set11)
#   discard(item):从集合中移除指定对象item，元素item不存在不影响，不会抛出Keyerror错误
set12 = {"ab","cd","ef"}
set12.discard("g")
print(set12)
#pop()：随机从集合中移除并返回一个元素；入参：无；返回：被移除的元组；如果集合为空则会引发KeyError
set13 = {1,7,3,4,5}
print(set13.pop(),set13)
print(set13.pop(),set13)
#   clear():清空集合，移除所有元素
set14 = {1,2,3,4,5}
set14.clear()
print(type(set14),set14)
"""
集合运算
交集运算
并集运算
差集运算
"""
"""
交集运算
intersection()
操作符：& 
"""
a = {1,2,3}
b = {1,4,5}
print(a.intersection(b))
print(a & b)
#   集合运算：并集 union（）；操作符：|
c = {1,2,3}
d = {1,2,5,6}
#两个集合的所有惟一值
print(c.union(d))
print(c | d)

#集合运算：差集；属于集合a不属于集合b的元素；difference（）；操作符：-
e = {1,2,3,4}
f = {1,6,7,8}
print(e.difference(f))
print(f - e)

"""
集合推导式
"""
set15 = {i for i in "hello" if i in "element"}
print(set15)
# 使用for循环找到"hello"和"element"中的共同元素
a = {"hello"}
b = {"element"}
c = set()
for i in "hello":
    if i in "element":
        c.add(i)
print(c)
#   使用for循环找到"hello"和"element"中的共同元素
d = { i for i in "hello" if i in "element"}
print(d)