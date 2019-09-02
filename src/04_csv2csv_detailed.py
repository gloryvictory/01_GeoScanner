#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author  :   Viacheslav Zamaraev
#   email   :   zamaraev@gmail.com
#   Date    :   15.07.2019
#   Copyright   : (C) 2019 by Viacheslav Zamaraev
#   Desc    :   script for converting csv to detailed csv for analysing in BI or Excel


#import os
#import datetime
from datetime import datetime
import logging
#import sys
#import string
import csv


def setup_logger(logger_name='log', level=logging.INFO):
    log_file = logger_name + '.log'
    lll = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setFormatter(formatter)
    lll.setLevel(level)
    lll.addHandler(file_handler)


def init_log_file():
    setup_logger('02_All_Statistics')
    logger = logging.getLogger('02_All_Statistics')
    logger.info("Program started")
    return logger


def file_csv_load(file_name=''):
    with open(file_name, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';', quotechar='"')  # some settings
        for row in csv_reader:
            print(', '.join(row))

    csvfile.close()


def main():
    time1 = datetime.now()
    print('Starting at :' + str(time1))

    # set some global variables
    # global _delimiter
    # _delimiter = ';'
    #
    # global _quotechar
    # _quotechar = '"'

    global _log
    _log = init_log_file()


    file_csv = 'test.csv'
    # for files in os.listdir(logsdir):  # Find all the files in the directory
    #     if files.endswith(".csv"):
    file_csv_load('test.csv')


    #ScanDisk()

    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')
    _log.info("Duration scan script: " + str(time2 - time1))


if __name__ == '__main__':
    main()
