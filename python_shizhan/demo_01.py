import os
import configparser
import logging

current_path = os.path.dirname(__file__)
conf=configparser.ConfigParser()
conf_path = os.path.join(current_path, '../config/config.ini')
conf.read(conf_path,encoding="utf-8")
a=conf.get('default','excel_path')
print(a)

logger= logging.getLogger(__name__)