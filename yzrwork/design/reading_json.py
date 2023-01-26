import json
import os
import re

file_path = "json/test.json"

read_json = open(file_path, 'r')   #ファイルを開く
json_load = json.load(read_json)   #開いたファイルをJSONとして読み込む
JSON_MAIN = json_load["main"]    #test.jsonのmainの部分
first_key = []   #first_keyという空のリスト作成
first_value = []    #first_valueという空のリストを作成
value = []

for get_json in JSON_MAIN:
    first_key.append(get_json)
    first_value.append(JSON_MAIN[get_json])
    second_key = []
    second_value = []
    if re.search(r"{", str(JSON_MAIN[get_json])):
        for secondkey in JSON_MAIN[get_json]:
            second_key.append(get_json)
            second_value.append(JSON_MAIN[get_json])
            if re.search(r"{", str(JSON_MAIN[get_json][secondkey])):
                print(JSON_MAIN[get_json][secondkey])
            else:
                value.append(JSON_MAIN[get_json][secondkey])
    else:
        value.append(JSON_MAIN[get_json])
print(value)
    
    

