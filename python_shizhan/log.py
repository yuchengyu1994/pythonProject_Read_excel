import os
import logging

current_path=os.path.dirname(__file__)
logger= logging.getLogger(__name__)  #创建一个日志对象 (__name__ 定义一个名称)
log_path=os.path.join( current_path,'../log_data/log.txt')
logger.setLevel(level= logging.INFO)  #设置全局日志的级别 debug info warning error ....
console= logging.StreamHandler()      #创建一个控制台输出日志的对象
formatter = logging.Formatter('file:%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
file_log=logging.FileHandler(log_path)
file_log.setFormatter(formatter)
logger.addHandler(console)            #日志对象配置在控制台输出
logger.addHandler(file_log)
logger.info('hello,world')  #替换我们之前的print
logger.setLevel(level= logging.ERROR)  #设置全局日志的级别 error
logger.error('hello,world')