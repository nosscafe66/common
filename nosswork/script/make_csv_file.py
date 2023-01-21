# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = ""
__prodactname__ = ""

import os
import sys
import glob
import logging
import re
from pathlib import Path
from datetime import datetime, timedelta

path=(__file__)
args=sys.argv
extension=args[1]
now_datetime = datetime.now()
file_date = now_datetime.strftime('%Y%m%d%H%M%S')

#メイン処理
def main():
    try:
        file_list,replace_path = read_py_file(path,extension)
        numbering_file_list = numbering(file_list)
        text_file = csv_make_file(numbering_file_list,replace_path,file_date)
        csv_file = repalace_file_name(text_file,replace_path)
    except Exception as e:
        logging.error(e)
        exit(1)
        raise

#①フォルダ配下のpythonファイルを読み取る
def read_py_file(path,extension):
    replace_path = path.replace(path.split('\\')[3],"")
    print(replace_path)
    search_file_list = []
    file_list = glob.glob(replace_path + "/*")
    for file in file_list: 
        match = re.search("\.{}$".format(extension), file)
        if match: 
            search_file_list.append(file)
            print(f".{extension}ファイルは:", file)
    return search_file_list,replace_path
    
#②取得したファイル名に連番を振る
def numbering(file_list):
    numbering_file_list = []
    for index,file_num in enumerate(range(len(file_list))):
        numbering_file_list.append(f"{index},{file_list[file_num]}")
    return numbering_file_list
    
#③空の出力ファイルを作成する。
def csv_make_file(numbering_file_list,replace_path,file_date):
    text_file = f"{replace_path}output_{file_date}.txt"
    with open(text_file, "wt",encoding='utf-8') as f:
        for text_num in range(len(numbering_file_list)):
            f.write(f"{str(numbering_file_list[text_num])}\n")
            print(str(numbering_file_list[text_num]))
    return text_file

#拡張子を「.txt」から「.csv」へ変更する。
def repalace_file_name(text_file,replace_path):
    repalace_file_name = text_file.replace(f"{replace_path}{text_file}",f"{replace_path}output.csv")
    for f in Path(replace_path).rglob('*.txt'):
        f.rename(replace_path + f.stem + '.csv')
    return repalace_file_name

if __name__ == "__main__":
    main()