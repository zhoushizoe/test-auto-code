#  顺序结构：一条一条语句顺序执行叫做顺序结构 分支判断
#  分支结构：在某个判断条件后，选择一条分支去执行
#   if 条件判断,if后边有冒号
zoe = "beautiful"
if zoe == "ugly":
    print("you are so beautiful;")
#   else 判断语句
zoe = "stupid"
if zoe == "smart":
    print("zoe is good")
else:
    print("please choose a other persion")
#   elif 多重条件
weather = "cloudy"
if weather == "shine":
    print("今天是大晴天")
elif weather == "cloudy":
    print("今天是多云")
elif weather == "foggy":
    print("今天有雾")
elif weather == "thunderstorm":
    print("今天有雷雨")
else:
    print("今天的天气很特别")

#   分支嵌套
fruits = "grape"
colour = "purple"
if fruits == "apple":
    colour == "red"
    print("这是一个红色的苹果")
elif fruits == "banana":
    if colour == "yellow":
        print("这是一个黄色的香蕉")
#   优化后的分支嵌套方法
elif fruits == "grape" and colour == "purple":
    print("这是一个紫色的葡萄")
#   三目运算符,判断语句与条件语句同时存在
nummber = 1
math = 2
if nummber > math:
    name = "zor"
else:
    name = "zoe"
print(name)
#   高级一点的写法，赋值语句写在最前边，if 判断语句，else需要赋值的内容，无冒号
page1,page2 = 5,9
s = "happy" if page1 > page2 else "bob"
print(s)