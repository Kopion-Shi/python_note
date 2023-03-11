# -*- coding: utf-8 -*-
# @Time    : 2023/3/5 16:43
# @Author  : 石鑫磊
# @Site    : 
# @File    : get_config.py
# @Software: PyCharm 
# @Comment :
import os
import os
import sys
from configparser import ConfigParser

from settings import base_file

file_path = '/config/logging.conf'
file_path = os.path.join(base_file + file_path)

config = ConfigParser()

print(file_path)

config.read(file_path, encoding='utf-8')

print('lang>name:', config['loggers']['keys'])
