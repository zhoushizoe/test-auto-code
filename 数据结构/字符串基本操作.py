#单行、多行
str_a = "this is my python"
str_b = """
this is my python
i will turn my line
"""
print(str_a)
print(str_b)
#转义字符  \n换行符
print("i love python \n no,i don't")
#  %s：格式化字符串的使用，"我是一个"替换掉%s的位置
#  %d：格式化整数
print("i am a %s"%"我是一个")
#   字符串之字面量插值："str.format"
#   不设置指定位置，按默认顺序
str_format1 = "字符串字面量插值? {}"
format_2 = str_format1.format("你以为我学会了？其实我没有")
print(format_2)
#   第一个参数放在0的位置，第二个参数放在1的位置
str_format2 = "i am very {1} {0}"
format_3 = str_format2.format("persion","yes")
print(format_3)
#   使用变量传递参数
str_format3 = "you are a very {chara}"
format_4 = str_format3.format(chara="happy persion")
print(format_4)
#   f{变量},字符串前面添加f，变量使用{变量名}
name = "zoe"
mood = "happy"
print(f"my name is {name},i am very {mood}")
#   字符串常用api之join，列表转换为字符串,根据想要的格式拼接成字符串
join_1 = ["h","a","p","p","y"]
print("|".join(join_1))
#   字符串常用api之split，数据切分操作，根据split内的内容将字符串进行切分,切分后，以什么内容切分，什么内容就会没有
split_1 = "what the"
print(split_1.split(" "))
print(split_1.split("t"))
#   字符串常用api之replace，将目标的字符串替换为想要的字符串
replace_1 = "my name is zhou"
print(replace_1.replace("zhou", "zoe"))
#   字符串常用API之strip，去掉首尾的空格
strip_1 = " i am a human "
print(strip_1)
print(strip_1.strip())