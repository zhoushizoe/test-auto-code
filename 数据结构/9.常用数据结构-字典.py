"""
字典/映射/哈希表
允许存储一个键值对集合
python字典的关键特性在于解释器会通过键去查找值
"""
"""
 字典定义
    字典是无序的键值对集合
    字典用大括号{}包围
    每个键/值对之间用一个逗号分隔
    各个键与值之间用一个冒号分隔
    字典是动态的
"""
"""
创建字典
    使用大括号填充键值对
    通过构造方法dict（）
    使用字典推导式
"""
#   通过大括号填充键值对
dict1 = {"name":"xiaoming","sex":"men","age":"18"}
print(dict1)
#   创建一个空字典
dict2 = {}
print(dict2)
#   通过构造方法dict()
#   通过构造方法构造一个空字典
dict3 = dict()
print(dict3)
#   传入一个带有元组的列表
dict4 = dict([("name","daming"),("sex","women")])
print(dict4)
dict5 = dict((["name","nihao"],["haoma","haode"]))
print(dict5)

#   使用字典推导式
dict6 = {i:v for i,v in [("name","daming"),("sex","women")] }
print(dict6)

"""
字典使用：访问元素
    与字典也支持中括号记法[key]
    字典使用键来访问其关联的值
    访问时对应的key必须要存在
"""
dict7 = {"what":"aha","where":"en?","who":"haha"}
#   提取键"what"来找寻对应的值"aha"
print(dict7["what"])
#   使用不存在的key，会报keyerror的错误
# print(dict7["age"])
"""
字典使用：操作元素
语法：dict[key] = value
    添加元素：键不存在
    修改元素：键已经存在
"""
dict8 = {"name":"lihua","sex":"men"}
dict8["age"] = "18"
print(dict8)
dict8["name"] = "xiaohua"
print(dict8)
"""
字典使用：嵌套字典 
字典的值可以是字典对象
"""
dict9 = {"persion":{"name":"xiaoming","sex":"man"},"chara":"outgoing"}
print(dict9["persion"]["name"])
dict9["persion"]["sex"] = "woman"
dict9["persion"]["age"] = "20"
print(dict9)

"""
字典常用的一些方法
key():获取所有的键
values()：获取所有的值
items()：获取字典所有的键值对成对的对象
get()：获取某个键的值
update()：更新字典
pop()：删除某个键值对
"""
dict10 = {"who":"z","where":"library","when":"now","what":"learn_python"}
dict11 = {"who":"s","where":{"library":"home","company":"supermarket"}}
#   keys：获取所有的键的值,返回由字典键组成的一个新的视图对象
di = dict10.keys()
print(type(di),di)
for key in di:
    print(key)
#   values：获取所有的值
print(dict10.values())
print(dict11.values())
#   将获得的values转成列表
print(list(dict10.values()))
#   item：获取字典所有的键值对成对的对象
print(dict10.items())
print(dict11.items())
#   get方法：获取某个键的值，不会产生keyerror错误，没有值返回none
print(dict10.get("who"))
print(dict11.get("where"))
print(list)
#   更新字典,update(dict),使用来自dict的键或值，覆盖原用的键或值;使用新的值会直接使用
print(dict10.update({"who": "zhangsan", "where": "lisihome"}))
print(dict10)
dict10.update(dict11)
print(dict10)
#   pop（key）：删除指定key的键值对，并返回对应的value值
#   入参：key必填，如果key存在在字典中，则将其移除并返回value值
#   如果key不存在与字典中，则会引起keyerror
print(dict10.pop("who"))
print(dict10)

"""
字典推导式：可以从任何以键值对作为元素的可迭代对象中构建出字典
"""
#   实例：给定一个字典对象{"a":1,"b":2,"c":"3"},找出其中所有大于1的键值对，同时value值进行平方运算
example = {"a":1,"b":2,"c":3}
data = {}
for k,v in example.items():
    if  v > 1:
        #   将改变的v值赋值到原来的k值上
        data[k] = v**3
print(data)

dict12 = {k:v**2 for k,v in example.items() if v >1}
print(dict12)
dict13 = {k:v for k,v in [("a","b"),("c","d")] }
print(dict13)

"""
给定一个字典对象，请用字典推导式，将key和value值进行交换
"""
a = {"a":1,"b":2,"c":3}
b = { v:k for k,v in a.items() }
print(b)