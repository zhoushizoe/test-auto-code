a = 1
print(a)
int_a = 1
print(type(int_a))
float_a = 2.0
print(type(float_a))
#求==两边的数据是否相等
eq_1 = 2==3
print(eq_1)
#求!=两边的数据是否不相等
uneq_1 = 2!=3
print(uneq_1)
#字符串格式需要加双引号，可以打印任意字符
str_a = "i am learning python"
print(str_a)
print(type(str_a))
#  \n是换行的意思，如果要忽略就再加一个\
str_b = "abc\ni love you"
print(str_b)
#r：忽略转义符
str_c = r"abc\n i love you "
print(str_c)
#+号，多个字符串连接
str_d = (str_a + str_b)
print(str_d)
#索引：字符串第一个位置索引为0,索引打印：print(var[索引])
var = "1234567"
print(var[0])
#切片:print(var_1[1:5])，前闭后开原则
var_1 = "1234567"
print(var_1[1:5])
print(var_1[1:])
#步长：print(var_2[0:8:2])，每隔两个取一个[start:stop:step]
var_2 = "1234567"
print(var_2[0:8:2])
#列表,[]里边可以放任何类型
list_1 = [1,2,3,4,"a","b",True]
print(list_1)
#列表也有切片的作用,倒数第一位用-1
list_2 = [1,2,3,4,5,6]
print(list_2[-1])
print(list_2[0::2])
print(list_2[0])


