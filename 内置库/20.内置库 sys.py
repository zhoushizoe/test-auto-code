"""
sys模块
    python自带的内置模块
    是与python解释器交互的桥梁
"""
# 导入sys模块
import os.path
import sys
import time
# 查看sys模块帮助文档
# help(sys)
# # 查看sys模块的属性和方法
# print(dir(sys))
"""
sys常用属性：
    sys.version：返回python解释器版本
    sys.platform:返回操作系统平台名称
    sys.argv:返回外部向程序传递的参数
    sys.modules:返回已导入的模块信息
    sys.path:返回导包的搜索路径列表
"""
# sys.version：返回python解释器版本
print(sys.version)
# sys.platform:返回操作系统平台名称；linux：返回的是linux；windows系统返回win32；macos返回darwin
print(sys.platform)
# sys.argv:返回外部向程序传递的参数
print(sys.argv)
# sys.modules:返回已导入的模块信息
print(sys.modules)
print(sys.modules.keys())
# sys.path:返回导包的搜索路径列表
print(sys.path)
# 添加自定义路径到导包路径列表中
# my_dir = os.path.dirname(os.path.abspath(__file__)) + "/TEST"# 获取当前目录的绝对路径
my_dir = os.path.dirname(os.path.abspath("20.内置库 sys.py")) + "/TEST"
sys.path.append(my_dir)
from TEST import test
test()

"""
sys常用方法
sys.getdefaultencoding():获取编码方式
sys.exit():运行时退出
"""
# sys.getdefaultencoding():获取编码方式
print(sys.getdefaultencoding())
# sys.exit():运行时退出
for i in range(10):
    if i == 6:
        print("exit...")
        sys.exit("程序退出")
    print(f"running{i}...")
    time.sleep(1)


