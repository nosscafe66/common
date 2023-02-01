# coding: utf-8
# whileによるループ処理

i = 1 #カウンタ変数を初期化
while i <= 10:
    print(i) #繰り返し処理
    i += 1 #カウンタ変数を更新する処理(カウンタ変数を更新する処理を書かないと、ずっと処理が終了しない)
    print("next:" + str(i))
    
print("last:" + str(i))