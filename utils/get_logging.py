# -*- coding: utf-8 -*-
# @Time    : 2023/3/5 16:20
# @Author  : 石鑫磊
# @Site    : 
# @File    : get_logging.py
# @Software: PyCharm 
# @Comment :
import logging
import logging.config
import os

from settings import base_file

file_path = '/config/logging.conf'
file_path = os.path.join(base_file + file_path)

class GetLogger():

    instance=None

    # def __new__(cls, *args, **kwargs):
    #     if cls.instance:
    #         return cls.instance
    #     cls.instance=object.__new__(cls)
    #     return cls.instance

    def app01Logging(self,confName="applog"):
        logging.config.fileConfig(file_path)
        return logging.getLogger(confName)

    def rootLogging(self,confName="root"):
        logging.config.fileConfig(file_path)
        return logging.getLogger(confName)


if __name__ == "__main__":
    _logger_root=GetLogger().rootLogging()
    _logger_app=GetLogger().app01Logging()

    _logger_root.debug('123')
