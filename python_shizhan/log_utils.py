import os
import logging
from python_shizhan.conf_until import read_config


print(read_config.get_logpath)
class LogUtils:
    def __init__(self,logfile_path=read_config.get_logpath):
        self.logfile_path=logfile_path
        self.logger=logging.getLogger()
        self.logger.setLevel(level= logging.INFO)
        formatter = logging.Formatter('file:%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_log = logging.FileHandler(self.logfile_path)
        file_log.setFormatter(formatter)
        self.logger.addHandler(file_log)

    def info(self,info_msg):
        self.logger.info(info_msg)

    def error(self,error_msg):
        self.logger.error(error_msg)
log_pri=LogUtils()
if __name__=='__main__':
    log1=LogUtils()
    log1.info('123')


