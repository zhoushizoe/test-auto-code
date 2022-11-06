"""
loggers：
handlers
filters：
formatters"
"""
import logging
logger = logging.getLogger("one logger")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()  # logging.FileHandler("文件名",encoding='utf-8')输出到文件中
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.debug("this is a debug")
logger.warning("this is a warn")
logger.info("this is a info")