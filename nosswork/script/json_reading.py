# -*- coding: utf-8 -*-
from pathlib import Path
import re
import logging
import glob
import sys
import os
import json
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

#メイン関数
def main():
    value = json_read(JSONFILENAME)
    print(value)
    transform_json_value(value)

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
    pass


if __name__ == "__main__":
    main()
