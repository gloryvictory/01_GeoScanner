#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author  :   Viacheslav Zamaraev
#   email   :   zamaraev@gmail.com
#   Date    :   15.07.2019
#   Copyright   : (C) 2019 by Viacheslav Zamaraev
#   Desc    :   script for finding geodata (shp, mif/mid, gps ...) and metadata and all data on Windows/linux/mac disks


import os
#import datetime
from datetime import datetime
import logging
import sys
import string


def setup_logger(logger_name = 'log', level=logging.INFO):
    log_file = logger_name + '.log'
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    # streamHandler = logging.StreamHandler()
    # streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    # l.addHandler(streamHandler)


def InitLogFile():
    setup_logger('02_All_Statistics')
    logger = logging.getLogger('02_All_Statistics')
    logger.info("Program started")
    return logger


def main():
    time1 = datetime.now()
    print('Starting at :' + str(time1))

    global LOGGER
    LOGGER = InitLogFile()


    #ScanDisk()

    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')
    LOGGER.info("Duration scan script: " + str(time2 - time1))


if __name__ == '__main__':
    main()