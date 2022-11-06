"""#   python 常用数据结构
#   list 列表：有序的顺序
#   tuple元组：有序的顺序
#   set集合：唯一性
#   dict字典：数据的结构很关键
"""
"""  列表的定义与使用
#       列表是有序的可变元素的集合，使用中括号[]包围，元素之间用逗号分割
#       列表是动态的，可以随时扩展和收缩
#       列表是异构的，可以同时存放不同类型的对象
#       列表中允许出现重复元素
#   列表的常用方法
#       创建列表
#           通过构造函数创建 list（）
"""
li = list()
print(type(li),li)
li1 = list("today is happy day")
print(type(li1),li1)
#           中括号创建并填充
li2 = [1,2,3,4,5,6,7,8]
li3 = ["nihao",2456,5,[5,6]]
print(li2,li3)
#           列表推导式
li4 = [i for i in range(2,11,2)]
print(li4)
"""列表使用：索引
默认正向索引，标号从0开始
 支持反向索引，标号从-1开始"""
li5 = [1,3,5,7,9]
print(li5[2])
print(li5[-2])
"""
    切片[start:stop:step]
    start值：指示开始索引值，如果没有制定，默认开始值为0
    stop值：指示到哪个索引值结束，但不包括这个结束索引值。如果没有指定，则取列表允许的最大索引值
    step值：步长值指示每一步大小，如果没有指定，则默认步长值为1。
    三个值都是可选的，非必填
"""
li6 = ["第一个",2,"第三个",4,"第五个",6]
print(li6[2::])
print(li6[0:5:2])
print(li6[::2])
print(li6[2:4:])
print(li6[::-1])
"""
列表使用：运算符
重复：使用*运算符可以重复生成列表元素
合并：使用+加号运算符可以将两个列表合二为一
"""
li7 = [1,2,3]
li8 = li7 * 5
li9 = li7 + li6
print(li8)
print(li9)
"""
列表使用：成员检测
    in：检查一个对象是否在列表中，如果在则返回Ture，否则返回False
    not in：检查一个列表是否不包括某个元素。如果不在返回Ture，否则返回False
"""
li10 = ["nihao","","hello",1019]
print("nihao" in li10)
print("hall" in li10)
print("nihao" not in li10)
print("hall" not in li10)
"""
列表方法:
apend()
extend()
insert()
pop()
remove()
sort()
reverse()
"""
#   append(item):将一个对象item添加到列表的末尾
#   入参：对象item；返回：None
li11 = []
li11.append("第一个")
li11.append("第二个")
li11.append(3)
li11.append(4)
print(li11)
# 打印列表的长度
print(len(li11))
#   extend（iterable）：将一个可迭代对象的所有元素，添加到列表末尾
#   入参：可迭代对象iterable；返回：None
li11.extend("extend")
print(len(li11),li11)
li12 = ["a","b","c"]
#li12添加到li11里
li11.extend(li12)
print(len(li11),li11)
#   insert（index，item）：将一个对象插入到指定的索引位置；入参：索引值index，一个对象item，原索引位置及后边的位置后移一位
li13 = [1,2,3,4,5]
li13.insert(2,"插入到2的后边")
li13.insert(0,"添加到最前边")
print(len(li13),li13)
"""
pop(index)或Pop()，弹出并返回所指定索引的元素
入参：索引值index，可不传
返回：指定索引的元素
返回：为指定索引则返回末端元素
如果索引值不正确，或者列表已经为空，则引发IndexError错误
"""
li14 = [1,2,3,4,5,6,7]
data = li14.pop(2)
print(li14)


"""
remove(item)
移除列表中第一个等于item的元素
入参：指定元素item
返回：None
目标元素必须已存在，否则会报ValueError
"""
li15 = [1,2,2,4,5,6]
print(li15)
remove_1 = li15.remove(2)
print(remove_1,li15)

"""顺序类的方法：sort"""
"""
列表方法sort(key=None,reverse=False),对列表进行原地排序，只使用<来进行各项间比较
入参：key：指定带有一个参数的函数，用于从每个列表元素中提取比较键
reverse：默认值为False表示升序，为Ture表示降序
返回：None
"""
#   sort函数，使乱序的列表进行升序排列
li16 = [1,4,3,6,7,8,]
li16.sort()
print(li16)
#   li16倒序排列
li16.sort(reverse=True)
print(li16)
#   按照字符串长度排列
li17 = ["abcdefg","ab","abc","abcde"]
li17.sort(key=len)
print(li17)
li17.sort(key=len,reverse=True)
print(li17)

"""
reverse()：将列表中的元素顺序反转；参数：无；返回：None，反转只是针对索引值，元素之间不相互比较
"""
li18 = [1,2,3,5,3,6,7]
li18.reverse()
print(li18)
"""
列表嵌套
嵌套列表是指在列表里存放列表
列表的常用方法都适用于嵌套列表
"""
#   打印嵌套列表中第二个列表的第三个元素
li19 = [[1,2,3,4],["ab","cd","ef"]]
print(li19[1][2])
#   在嵌套列表的第二个列表中添加新的元素
li19[1].append("gh")
print(li19)
"""
列表推导式
列表推导式是指循环创建列表，相当于for循环穿件列表的简化版
语法：[x for x in li if x...]
"""
#   将1-10中的所有偶数平方后组成新的列表
#   传统解决方案
result = []
for ele in range(1,11):
    if ele % 2 == 0:
        result.append(ele ** 2)
print(result)
#   使用列表推导式方案
result_2 = [ele ** 2 for ele in range (1,11) if ele % 2 == 0]
print(result_2)

result_3 = []
for ele in range(1,11):
    if ele % 2 == 0:
        result_3.append(ele ** 2)
print(result_3)
result_4 = [ele ** 2 for ele in range(1,11) if ele % 2 != 0]
print(result_4)
