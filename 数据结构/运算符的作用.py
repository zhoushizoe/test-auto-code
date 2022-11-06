#   + 加
1 + 1
#   - 减
2 - 1
#   * 乘
3 * 2
#   / 除
3 / 2
#   % 取余
3 % 2
#   ** 幂
3 ** 2
#   // 取整除
3 // 2


#   比较运算符，输出的是布尔值
#   == 等于
#   != 不等于
#   > 大于
#   < 小于
#   >= 大于等于
#   <= 小于等于
a = 3
b = 4
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#   赋值运算符
# = 简单赋值运算符,右边赋值给左边
a = 1
b , c = 2 , 3
print(a,b,c)
# 自增操作
# += 加法赋值运算符,下边两个相等
h = 3
h = h+3
h += 3
#  -= 减法赋值运算符，以下两个等式相同
e = 3
e = e-3
e -= 3
#  *= 乘法赋值运算符
#  /= 除法赋值运算符
#  %= 取模赋值运算符
#  **= 幂赋值运算符
#  //= 取整赋值运算符

#   逻辑运算符，最终的结果是布尔值
#   and x and y；x，y都为真才是真，一个假即为假
#   or x or y；x、y有一个真即为真，都为假为假
#   not not x，如果x为假，则not x为真
f , g = True , False
print(f and g)
print(f or g)
print(not g)


#   成员运算符，in的右边为序列：字符串，元祖，列表等
#   in 如果在指定的序列中找到值返回Ture，否则返回False
#   not in 如果在指定的序列中没有找到值返回Ture，否则返回False
list_a = ["a","b","c","d"]
print("a" in list_a)
print("e" in list_a )
print("a" not in list_a)
print("e" not in list_a)

#   身份运算符，id，使用的内存地址
#   is 是判断两个标识符是不是引用自一个对象，判断两个变量之间的内存地址是否相同
#   is not 判断两个标识符是不是引用自不同对象
#   可变的数据结构，即使看着一样，但是数据地址是不同的，如果是不可变的数据类型，如果看着一样，他们的内存地址是相同的
a = "nihao"
b = "nihao"
print(id(a))
print(id(b))
print(a is b)
print(a is not b)
