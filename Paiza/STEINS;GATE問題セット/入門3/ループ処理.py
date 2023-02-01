# coding: utf-8
# 標準入力とループ処理

count = int(input())
# print("データ個数 " + str(count))
for i in range(count):
    line = input().rstrip() #rstripはデータの行末の改行を削除する
    print(line + "は、成功した")