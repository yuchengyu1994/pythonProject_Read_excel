import os
import configparser


current_path = os.path.dirname(__file__)
cfgpath='../config/config.ini'

class ReadConf:
    def __init__(self,conf_path=cfgpath):
        # self.conf_data=configparser.ConfigParser().read(conf_path)
        self.conf_path=conf_path
        self.conf = configparser.ConfigParser()
        self.conf.read(os.path.join(current_path, self.conf_path))

    def read(self,sec,name):
        # conf = configparser.ConfigParser()
        # conf.read(os.path.join(current_path, self.conf_path))
        return self.conf.get(sec,name)
    @property
    def get_excelpath(self):
        return self.read('default','excel_path')

    @property
    def get_logpath(self):
        return os.path.join(current_path,self.read('default', 'log_path'))

read_config=ReadConf()