"""
OS:Operating System：操作系统
os模块的常用功能
跨平台的差异
"""
"""
OS使用：
导入OS模块
查看os模块使用文档
    help（os）
    dir（os）
"""
# 导入os模块
import os
# 查看帮助文档
# help(os)
# 查看 os模块的一个属性和常用的方法
print(dir(os))
"""
os常用方法
系统相关
操作目录
操作路径
"""
"""
os操作系统相关
    os.name:获取系统名称
    os.envion:获取系统环境变量信息
    os.getenv('PATH'):获取指定名称的环境变量信息
    os.system():执行系统指令
"""
# os.name:获取系统名称;nt代表window，posix代表linux
print(os.name)
# os.envion:获取系统环境变量信息
print(os.environ)
# os.getenv('PATH'):获取指定名称的环境变量信息
print(os.getenv('PATH'))
# os.system():执行系统指令，获取当前的目录名称
print(os.system("pwd"))

"""
os目录相关
    os.getcwd():获取当前目录
    os.chdir()：切换目录
    os.listdir()：列出当前目录内容
    os.mkdir()：创建空目录
    os.makedirs()：递归创建多级目录
    os.rmdir():删除空目录
    os.rename()：重命名目录
    os.remove()：删除文件
"""
# # os.getcwd():获取当前目录
# print(os.getcwd())
# # os.chdir()：切换目录
# os.chdir("..")
# os.listdir()：列出当前目录内容
# print(os.listdir())
# os.mkdir()：创建空目录
# os.mkdir('new1')
# print(os.listdir())
# os.rename()：重命名目录
# os.rename('new', 'new2')
# print(os.listdir())
# os.rmdir():删除空目录
# os.rmdir('new2')
# print(os.listdir())
# os.rmdir('new1')
# print(os.listdir())

"""
os 路径相关
path方法
    os.path.abspath(path)   返回绝对路径
    os.path.basename(path)  返回文件名
    os.path.dirname(path)   返回文件路径
    os.path.split(path)     分割路径
    os.path.join(path)      拼接路径
    os.path.exists(path)    判断路径是否存在
    os.path.isdir(path)     判断是否是目录
    os.path.isfile(path)    判断是否是文件
    os.path.getsize(path)   获取文件大小
"""
# os.path.abspath(path)   返回绝对路径
# 获取当前文件的绝对路径
print(os.path.abspath("19.内置库 OS.py"))
# os.path.basename(path)  返回文件名,传入绝对路径
print(os.path.basename("//19.内置库 OS.py"))
# os.path.dirname(path)   返回文件路径,传入绝对路径
print(os.path.dirname("//19.内置库 OS.py"))
# os.path.split(path)     分割路径
print(os.path.split("//19.内置库 OS.py"))
# os.path.join(path)      拼接路径
print(os.path.join("/", "19.内置库 OS.py"))
# os.path.exists(path)    判断路径是否存在
print(os.path.exists("/"))
print(os.path.exists("/Users/mac/PycharmProjects/python_learn20221013"))
# os.path.isdir(path)     判断是否是目录
print(os.path.isdir("/"))
# os.path.isfile(path)    判断是否是文件
print(os.path.isfile("19.内置库 OS.py"))
print(os.path.isfile("19.内置库1 OS.py"))
# os.path.getsize(path)   获取文件大小 返回字节大小
print(os.path.getsize("//19.内置库 OS.py"))