"""
程序调试：程序调试是将编制的程序投入实际运行前，
        用手工或编译程序等方法进行测试，修正【语法错误和逻辑错误】的过程
语法错误：
        编写的python语法不正确，程序编译失败
 逻辑错误：
        代码本身能够正常执行，但是执行完成的结果不符合预期结果
"""
"""
调试方法：
    对应位置使用'print'或者'logging'打印日志信息
    启动断点模式debug调试
"""
# 打印日志
# 传入logging模块
import logging
# 设置打印日志的级别
logging.basicConfig(level=logging.INFO)
a = 1
b = 2
if a == 1:
    flag = True
    # print(f"a ==1 : flag = {flag}")
    # logging.info(f"a ==1 : flag = 13")
else:
    flag = False
    print(f"else: flag = {flag}")
