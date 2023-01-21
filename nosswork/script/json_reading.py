# -*- coding: utf-8 -*-
from pathlib import Path
import re
import logging
import glob
import sys
import os
import json
import logging
from datetime import datetime, timedelta
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__ = ""
__prodactname__ = ""


ARGS = sys.argv
JSONFILENAME = ""
PATH = (__file__)
DIRNAME = os.path.dirname(__file__)
BASENAME = os.path.basename(__file__)
JSONFILENAME = str(DIRNAME).replace("script", "json") + "/" + ARGS[1]
NOW_DATETIME = datetime.now()
FILE_DATE = NOW_DATETIME.strftime('%Y%m%d%H%M%S')

#メイン関数
def main():
    try:
        value = json_read(JSONFILENAME)
        transform_json_value(value)
        sys.exit(0)
    except Exception as e:
        logging.error(e)
        raise

# jsonファイルののバリューを読み取る


def json_read(JSONFILENAME):
    read_json_file_name = open(JSONFILENAME)
    json_value = json.load(read_json_file_name)
    JSON_MAIN_BODY = json_value["main"]
    first_value_arr = []
    first_key_arr = []
    value = []
    for firstkey in JSON_MAIN_BODY:
        first_key_arr.append(firstkey)
        first_value_arr.append(JSON_MAIN_BODY[firstkey])
        second_value_arr = []
        second_key_arr = []
        if re.search(r"{", str(JSON_MAIN_BODY[firstkey])):
            for secondkey in JSON_MAIN_BODY[firstkey]:
                second_key_arr.append(firstkey)
                second_value_arr.append(JSON_MAIN_BODY[firstkey])
                if re.search(r"{", str(JSON_MAIN_BODY[firstkey][secondkey])):
                    print(JSON_MAIN_BODY[firstkey][secondkey])
                else:
                    value.append(JSON_MAIN_BODY[firstkey][secondkey])
        else:
            value.append(JSON_MAIN_BODY[firstkey])
    return value

# 読み取ったバリューの値を変換する。


def transform_json_value(value):
    OUTPUTFILENAME=f'output_{FILE_DATE}.csv'
    with open(OUTPUTFILENAME,"wt") as f:
        for index,i in enumerate(range(len(value))):
            f.write(f'{index},{value[i]}\n')

if __name__ == "__main__":
    main()
