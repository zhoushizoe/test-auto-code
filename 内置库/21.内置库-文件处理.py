"""
IO:input和output
输入流：磁盘、网络流向内存
输出流：内存流出磁盘、网络
"""
"""
文件操作步骤：
打开文件
操作文件：读/写内容
关闭文件：（读写完成，要及时的关闭）
"""
"""
open方法：
def open(file,mode = "r",buffering = None,encoding = None,
        erroes = None,newline = None,closefd =  Ture)
file:文件路径
mode：读写方式
    r：以只读的方式打开文件，并将文件指针指向文件头，如果文件不存在会报错
    w：以只写模式打开文件，并将文件指针指向文件头，如果文件存在则将其内容清空，如果文件不存在则创建
    a：以只追加可写模式打开文件，并将文件指针指向文件尾部，如果文件不存在则创建
    r+：在r的基础上增加了可写功能
    w+：在w的基础上增加了可读功能
    a+：在a的基础上增加了可读功能
    b：读写二进制文件（默认是t，表示文本），需要与上边几种模式搭配使用，如ab，wb，ab+（POSIX系统，包括Linux都会忽略该字符）
buffering:缓冲区的大小
读取模式；encoding，中文乱码
erroes：遇上异常是忽略还是抛出来
newline：换行符，确定的换行符是哪个？
"""
"""
实战步骤：
    1.（以只读模式），打开文件
    f= open("/Users/mac/PycharmProjects/python_learn2022/内置库/file deal.text","r",encoding = "utf-8")
    2.读取文件内容
    print(f.read())
    3.关闭文件
    f.close()
"""
# def open("",mode = "r",buffering = None,encoding = None,
#         erroes = None,newline = None,closefd =  Ture)
import os
print(os.path.abspath("file deal.text"))
f = open("file deal.text", "r", encoding="utf-8")
print(f.read())
f.close()
"""
读操作：
read:一次读取文件所有内容，返回一个str
read（size）：每次最多读取指定长度的内容，返回一个str；在python2中size指定的是字节长度，在python3中size指定的是字符长度
readlines（）：一次读取文件所有内容，按行返回一个list
readline（）：每次只读取一行内容
"""
# read（size）：每次最多读取指定长度的内容，返回一个str；在python2中size指定的是字节长度，在python3中size指定的是字符长度
f = open("file deal.text", "r", encoding="utf-8")
print(f.read(2))# 换行符也是一个字符
f.close()
# readlines（）：一次读取文件所有内容，按行返回一个list
f = open("file deal.text", "r", encoding="utf-8")
print(f.readlines())
f.close()
# readline（）：每次只读取一行内容
f = open("file deal.text", "r", encoding="utf-8")
print(f.readline())
print(f.readline())
f.close()
"""
忘记关闭文件的危害
1.打开文件达到一定数量，将会导致打开失败
2.占用内存空间，非常浪费资源
3.会导致系统自动回收资源，而丢失数据
"""
"""
with用法：
在结束时自动的关闭
"""
with open("file deal.text", "r", encoding="utf-8") as f:
    print(f.read())
print(f.closed)
"""
写操作实战：
mode="w+",读写权限，会新建文件，清空内容再写入
mode="r+",读写权限，替换原来的内容
mode="a+",读写权限，追加内容
"""
# mode="w+",读写权限，会新建文件，清空内容再写入
print(os.path.abspath("write_1.text"))
# w = open("write_1.text", "r+", encoding="utf-8")
# print(w.write("第四行"))
# print(w.read())
# w.close()
# with open("write_2.text", "w+", encoding="utf-8") as w:
#     print(w.write("你好"))
# with open("write_1.text", "a+", encoding="utf-8") as a:
#     a.write("\n第二行")
a = open("write_1.text", "r", encoding="utf-8")
print(a.read())
a.close()

