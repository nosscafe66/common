# coding: utf-8
# 数の表示とサイコロ

import random

number = random.randint(1,100) #1〜100までの整数がランダムで表示される
print("スライムが" + str(number) + "匹現れた")


apple_price = random.randint(1,3)*100 #りんごの値段
apple_num = random.randint(1,10) #りんごの個数

print("りんごの値段：" + str(apple_price) + "円")
print("りんごの個数：" + str(apple_num) + "個")
total = apple_num * apple_price
print("合計金額：" + str(total) + "円")