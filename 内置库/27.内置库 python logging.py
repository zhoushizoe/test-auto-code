"""
日志作用
    调试
    辅助定位问题
    数据分析
"""
import os

"""
日志的级别
    DEBUG：细节信息，仅当诊断问题时适用
    INFO：确认程序按预期运行
    WARNING：表明有已经或即将发生的意外（例如：磁盘空间不足）。程序仍按预期进行
    ERROR：由于严重的问题，程序的某些功能已经不能正常执行
    CRITICAL：严重的错误，表明程序已不能继续执行
日志的用法：https://docs.python.org/zh-cn/3/howto/logging.html
    logging.debug(msg,*args,**kwargs):创建一条严重级别为DEBUG的日志记录
    logging.info(msg,*args,**kwargs):创建一条严重级别为INFO的日志记录
    logging.warning(msg,*args,**kwargs):创建一条严重级别为WARNING的日志记录
    logging.error(msg,*args,**kwargs):创建一条严重级别为ERROR的日志记录
    logging.critical(msg,*args,**kwargs):创建一条严重级别为CRITICAL的日志记录
    logging.log(level,*args,**kwargs):创建一条严重级别为level的日志记录
    logging.basicConfig:对root logger进行一次性配置
    
"""
import logging
# logging 默认设置的级别是warning
# 设置成哪种级别的的日志，就会打印这个级别及以上级别的日志
# logging.basicConfig(level=logging.INFO)
# logging.warning('Watch out!')  # will print a message to the console
# logging.info('I told you so')  # will not print anything
# logging.error("this is a error massage")
# 输出到命令行。INFO 消息并没有出现，因为默认级别是 WARNING 。
# 打印的信息包含事件的级别以及在日志调用中的对于事件的描述，例如 “Watch out!”。
# 暂时不用担心 “root” 部分：之后会作出解释。输出格式可按需要进行调整，格式化选项同样会在之后作出解释。
"""
设置日志的级别
logging.basicConfig(level = logging.INFO)
"""
"""
将打印出来的日志保存到文件中
"""
# logging.basicConfig(filename='example1.log', encoding='utf-8', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
# print(os.path.abspath("example1.log"))
# with open("/Users/mac/PycharmProjects/python_learn2022/内置库/example1.log", "r", encoding="utf-8") as f:
#     print(f.read())
'''
更改显示消息的格式
'''
# logging.basicConfig(format='%(asctime)s %(message)s')
# logging.warning('is when this event was logged.')
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.warning('is when this event was logged.')
# 设置成哪种级别的的日志，就会打印这个级别及以上级别的日志
# logging.error("this is a error info")
# logging.basicConfig(level = logging.INFO)
# logging.basicConfig(level=logging.INFO)
# logging.info("this is a info massage")
# 更改日志格式
# logging.basicConfig(format='%(asctime)s %(message)s')
# logging.basicConfig(format="%(asctime)s %(message)s")
# logging.error("this a error massage")
# 更改日期/时间显示的默认格式,datefmt的使用
# logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%m/%d/%Y")
# logging.error("this is a error massage")
# 打印超全日志
logging.basicConfig(filename="compile.log", level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)",
                    datefmt="%m/%d/%Y")
logging.info("this is a info message")
logging.error("this is a error message")