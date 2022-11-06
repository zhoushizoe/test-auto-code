"""
可变参数：
可变参数也称为不定长参数
传入参数中实际参数可以是任意多个
常见形式：*args；**kwargs
"""
"""
*args
接收任意多个实际参数，并将其放到一个元组中
使用已经存在的列表或元组作为函数的可变参数，可以在列表的名称前加*
"""
#   可以接收任意多个参数,并将其放在元组当中
def arg_1(*args):
    print(args)
#   遍历args中的所有元素
    for i in args:
        print(i)
arg_1("python","java","c++","c#","go","php")
lan = ["python","java","c++"]
#   以列表的形式展现语言
arg_1(lan)
#   一个解包操作，将列表里的元素拿出来
arg_1(*lan)

"""
**kwargs
接收任意多个类似关键词参数一样显式赋值的实际参数，并将其放到一个字典中
使用已经存在字典作为函数的可变参数，可以在字典的名称前加**
"""
def name_info(**kwages):
    print(kwages)
#使用kwages形式会得到字典key：value类型的值
name_info(tom="nihao",nana="hello",what="hah")
name2 = {"tom":"nihao","nana":"hello","what":"lala"}
# name_info(name2)
name_info(**name2)