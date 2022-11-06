#   循环：封装重复操作
#   for-in循环
#   使用场景：明确的知道循环执行的次数或者要对一个容器进行迭代
import random

a = [1,2,3,4,5] #元组，字符串，字典，可迭代元素
for i in a:
    print(i)
b = "12344"
for i in b:
    print(i)

#   range函数：range（101）可以产生一个0到100的整数序列
#   range函数：range（1，100）可以产生一个1到99的整数序列
#   range函数：range（1，100，2）可以产生一个1到99的奇数序列，其中的2是步长
for i in range(11):#range只有一个参数的时候，传入的是结束数值，前闭后开，相当于遍历一个数组
    print(i)
for o in range(2,11):#传入两个参数时，（开始数值，结束数值），前闭后开原则
    print(o)
for p in range(1,21,2):#传入三个参数，（开始数值，结束数值，步长），前闭后开原则
    print(p)
#   while循环
#   满足条件，进入循环，需要设定好循环结束的条件
a = 1
while a<6:
    print("123")
    a += 1
#   break-跳出整个循环体
#   1.不要直接使用2.注意设定的跳出条件
d = 0
while d < 5:
    d += 1
    if d == 3:
        break
    print(d)
e = 1
while e < 7:
    e += 2
    if e == 6:
        break
    print(e)
f = [1,2,3,4,5]
for i in f:
    print(i)
    if i == 4:
        break

#   continue跳出当前轮次循环
g = 1
while g<9:
    print(g)
    g += 1
    if g == 4:
        g += 2.4
        continue
#   for 循环与continue的使用
h = [7,0,33,4,77]
for i in h:
    if i == 4:
        continue
    print(i)
#   break 与continue的区别：break直接跳出循环，continue跳过本次

#   pass关键字，占位符，不影响代码逻辑
#计算1～100求和,使用分支结构
sum = 0
for i in range(2,101,2):
    sum = sum + i
    print(sum)
#   不使用分支结构计算1～100的求和
sum = 0
sum2 = 0
while sum < 100:
    sum += 2
    sum2 = sum2+sum
    print(sum2)

#   while 循环-实例
#猜数字游戏，计算机给出一个1-100之间的随机数由人来猜，计算机根据人猜的数字分别给出提示大一点、小一点、猜对了
#random需要传randint参数进来， 控制范围
import random
computer_num = random.randint(1,100)
#人传入的数字用input决定,可以输入数字，input默认输入字符串，做一个强制转换
#while True:
    #people_num = int(input("请输入你猜想的数字： "))
    #if computer_num > people_num:
            #print("大一点")
    #elif computer_num < people_num:
        #print("小一点")
    #else:
        #print("猜对了！")
        #break
#   不使用分支结构实现1～100之间的奇数求和
sum3 = 0
for i in range(1,100,2):
    sum3 = sum3 + i
    print(sum3)
#   使用while语句实现1～100之间的求和
j = 1
sum5 = 0
while j < 100:
    sum5 = sum5 + j
    j += 2
    print(sum5)






