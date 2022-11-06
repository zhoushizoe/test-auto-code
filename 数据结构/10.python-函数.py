"""
函数的作用、函数的定义、函数的调用、函数的传递、函数返回值
"""
"""
函数的作用：
函数是组织好的，可重复使用的，用来实现单一或相关联功能的代码段
函数能提高应用的模块性和代码的重复利用率
"""
"""
函数定义：
def：函数定义关键词
function_name：函数名称
()：参数列表放置的位置，可以为空
parameter_list:可选，指定向函数中传递的参数
comments：可选，为函数指定注释
function_body：可选，指定函数体
def function_name ([parameter_list])
    ['''comments''']
    [function_body]
"""


def first_def():
    '''没有参数的函数 '''
    print("this is a def")


# print(first_def())
def def_para_one(a, b, c):
    '''
    带有参数的函数
    :param a:
    :param b:
    :param c:
    :return:
    '''
    print(f"要传入的参数为：a={a},b={b},c={c}")


#   打印函数的注释
print(def_para_one.__doc__)
#   使用help打印函数的注释
help(def_para_one)


# 定义一个空函数的两种方式：
def fun_null(s):
    # 定义一个空函数的一种方式：使用占位符pass
    # 定义一个空函数的另一种方式：添加comment
    '''
    这是一个comment，可以不使用pass使空函数不报错
    '''
    pass


"""
定义函数的注意事项：
缩进：函数体和注释相对于def关键字必须保持一定的缩进，一般是四个空格，pycharm自动格式化快捷键：ctrl+alt+l
定义空函数：使用pass语句占位符；写函数注释comment
"""
"""
函数的调用
function_name：函数名称
parameter_value:可选，指定各个参数的值
"""
#   调用函数
first_def()
#   调用带参数的函数，传参
def_para_one(1, 2, 3)
"""
函数的参数区别
形式参数：定义函数时，函数名称后边括号中的参数
def fun_para(a,b,c)
实际参数：调用函数时，函数名称后面括号中的参数
fun_para(1,2,3)
位置参数：数量和位置必须与定义的时候一致
"""


def fun_judge(name, age):
    if age > 18:
        print(f"{name},你的年龄太大了，已经{age}岁了")
    else:
        print(f"{name},你的年龄是：{age}")


fun_judge("xiaohua", 23)
fun_judge("小周", 13)

"""
关键字传参：
使用形式参数的名字确定输入的参数值
不需要与形式参数的名字位置一致
"""


def fun_key(a,b,c):
    print(f"a是{a},b是{b},c是{c}")


fun_key(b=2, a=3, c=1)

"""
为参数设置默认值
定义函数时可以指定形式参数的默认值
指定默认值的形式参数必须放在所有参数的最后，否则就会出现语法错误
param = default_value：可选，指定参数并且为该参数设置默认值为default_value
"""


def fun_default(a, b, c=2):
    print(f"a = {a},b = {b},{c}的默认值是2")


fun_default(2, 3, 4)

"""
函数返回值：指定要返回的值return
"""


def sum_return(a,b):
    result = a + b
    return result, f"a为:{a}", f"b为：{b}"


sum1 = sum_return(2, 4)
print(sum1)
