#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author  :   Viacheslav Zamaraev
#   email   :   zamaraev@gmail.com
#   Date    :   10.01.2019
#   Copyright   : (C) 2019 by Viacheslav Zamaraev
#   Desc    :   script for finding geodata (shp, mif/mid, gps ...) and metadata and all data on Windows/linux/mac disks


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
import string



def get_list_from_file(file):

    lst = []
    with open(file, "r", errors='ignore') as f:
        lst = f.read().splitlines()
        if len(lst) > 2:
            lst[-1] = lst[-1].strip()  # удаляем последний \n
            # del lst[-1]
        f.close()
    return lst


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
    setup_logger('01_GeoScanner')
    logger = logging.getLogger('01_GeoScanner')
    logger.info("Program started")
    return logger


def ScanDir(dir_root=''):
    LOGGER.info("scan_directory")

    global PLATFORM
    global SEPARATOR
    global COMPNAME
    global FILE_CSV
    global CSV_SEPARATOR

    PLATFORM = platform
    SEPARATOR = os.sep
    CSV_SEPARATOR = ";"
    COMPNAME = platform.node()
    FILE_CSV = COMPNAME

    LOGGER.info("Platform is: " + str(PLATFORM))
    LOGGER.info("OS separator is: " + os.sep)
    LOGGER.info(os.environ)
    LOGGER.info(platform.uname())
    # dirname = '/Users/Macintosh/Desktop/Dropbox/MyPrj/MyGeo/01_GeoScanner/TestGeoData'

    if len(dir_root) == 0:
        dirname = str(os.getcwd())
    else:
        dirname = str(dir_root)

    # linux OR MAC OS X
    if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
        print(str(_platform))
        # dirname = str("/")
        dirname = '/Users/Macintosh/Desktop/Dropbox/MyPrj/MyGeo/01_GeoScanner/TestGeoData'

    # Windows or Windows 64-bit
    elif _platform == "win32" or _platform == "win64":
        print(str(_platform))
        available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
        LOGGER.info("Disk drives are " + str(available_drives))

        # dirname = available_drives[0] + SEPARATOR
        # LOGGER.info("Folder are " + str(dirname))
        file_name = COMPNAME + "_" + str(available_drives[0]).replace(":", "") + '.csv'
        with open(file_name, 'w') as f:
            f.write('$compname' + CSV_SEPARATOR + 'FullName' + CSV_SEPARATOR + 'Length' + CSV_SEPARATOR + 'CreationTime' + CSV_SEPARATOR + 'ModifiedTime' + CSV_SEPARATOR + 'AccessTime' + '\n')

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
                try:
                    filetime_c = str(datetime.fromtimestamp(os.path.getctime(filePath)).strftime('%Y-%m-%d %H:%M:%S'))
                    filetime_m = str(datetime.fromtimestamp(os.path.getmtime(filePath)).strftime('%Y-%m-%d %H:%M:%S'))
                    filetime_a = str(datetime.fromtimestamp(os.path.getatime(filePath)).strftime('%Y-%m-%d %H:%M:%S'))
                    filesize = str(os.path.getsize(filePath))
                    # f = open (filePath, 'r')
                    print(COMPNAME + ", " + filePath + ", " + filesize + ", " + filetime_c + ", " + filetime_m + ", " + filetime_a)

                except Exception as e:
                    LOGGER.error("Exception occurred", exc_info=True)



def main():
    time1 = datetime.now()
    print('Starting at :' + str(time1))

    global LOGGER
    LOGGER = InitLogFile()

    global file_exclude
    global LIST_EXCLUDE

    file_exclude = 'exclusions.txt'
    LIST_EXCLUDE = []
    try:
        if os.path.isfile(file_exclude):
            LIST_EXCLUDE = get_list_from_file(file_exclude)
            LOGGER.info("File exclusions found. Excludes folders count: " + str(len(LIST_EXCLUDE)))
        else:
            LOGGER.info("File not found: " + file_exclude)
            LIST_EXCLUDE = []
    except Exception as e:
        LOGGER.error("Exception occurred", exc_info=True)


    ScanDir('')
    #ScanDir('')




    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')


if __name__ == '__main__':
    main()