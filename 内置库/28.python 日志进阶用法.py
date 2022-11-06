"""
日志记录的流程
封装日志公共模块
日志配置文件
组件：
    loggers:提供应用程序代码直接使用的接口
    handlers：用于将日志记录发送到指定的目的位置
    filters：提供更细粒度的日志过滤功能，用于决定哪些日志记录将会被输出
    formatters：用于控制日志信息的最终输出格式
"""
import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()  # 如果是logging.FileHandler("mylog.log",encoding="utf-8),是以文件形式输出
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
