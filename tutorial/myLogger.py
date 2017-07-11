# -*-coding:utf-8 -*-
import logging


class MyLogger(object):
    def __init__(self, filename):
        # 创建一个logger
        self.logger = logging.getLogger('duan')
        self.logger.setLevel(logging.DEBUG)

        # 创建handler,写入日志
        fh = logging.FileHandler(filename + '.log')
        fh.setLevel(logging.DEBUG)

        # 创建handler，输出日志到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s >>> %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def info(self, data):
        self.logger.info(data)


if __name__ == '__main__':
    logger = MyLogger('logger')
    for i in range(0, 1000):
        logger.info(i)

