import logging.config
logging.config.fileConfig("logging.conf")
logger = logging.getLogger("main")
logger.debug("这是debug日志")
