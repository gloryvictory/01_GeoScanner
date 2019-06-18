#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author  :   Viacheslav Zamaraev
#   email   :   zamaraev@gmail.com
#   Date    :   10.01.2019
#   Copyright   : (C) 2018 by Luis Calisto and Andre Mano
#   Desc    :   script for finding geodata (shp, mif/mid, gps ...) and metadata


import os
#import datetime
from datetime import datetime
#, date, time
import logging
from sys import platform
import os
import platform
from sys import platform as _platform
import sys





def setup_logger(logger_name = 'log', level=logging.INFO):
    log_file = logger_name + '.log'
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    #streamHandler = logging.StreamHandler()
    #streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    #l.addHandler(streamHandler)

def InitLogFile():
    setup_logger('01_GeoScanner')
    logger = logging.getLogger('01_GeoScanner')
    logger.info("Program started")
    return logger


def ScanDir(dir = ''):
    LOGGER.info("test")

    global PLATFORM
    global SEPARATOR
    global COMPNAME

    PLATFORM = platform
    SEPARATOR = os.sep
    COMPNAME = platform.node()

    LOGGER.info("Platform is: " + str(PLATFORM))
    LOGGER.info("OS separator is: " + os.sep)
    LOGGER.info(os.environ)
    LOGGER.info(platform.uname())
    # dirname = '/Users/Macintosh/Desktop/Dropbox/MyPrj/MyGeo/01_GeoScanner/TestGeoData'

    # linux OR MAC OS X
    if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
        print(str(_platform))

    # Windows or Windows 64-bit
    elif _platform == "win32" or _platform == "win64":
        print(str(_platform))

    if len(dir) == 0:
        dirname = str(os.getcwd())
    else:
        dirname = str(dir)

    # for root, files in os.walk(dirname):
    #     for f in files:
    #         filepath = os.path.join(root, f)
    #         print(filepath)
    #
    # pass
    for root, subdirs, files in os.walk(dirname):

        for file in os.listdir(root):

            filePath = os.path.join(root, file)

            if os.path.isdir(filePath):
                pass

            else:
                # print(filePath)

                filetime_c = str(datetime.fromtimestamp(os.path.getctime(filePath)).strftime('%Y-%m-%d %H:%M:%S'))
                filetime_a = str(datetime.fromtimestamp(os.path.getatime(filePath)).strftime('%Y-%m-%d %H:%M:%S'))
                filesize = str(os.path.getsize(filePath))
                # f = open (filePath, 'r')
                print(COMPNAME + ", " + filePath + ", " + filesize + ", " + filetime_c + ", " + filetime_a)


def main():
    time1 = datetime.now()
    print('Starting at :' + str(time1))

    global LOGGER
    LOGGER = InitLogFile()

    ScanDir('')
    #ScanDir('')




    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')


if __name__ == '__main__':
    main()