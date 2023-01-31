# coding: utf-8
#  おみくじ作成

import random

omikuji = random.randint(1,10)
# 1:大吉 2:中吉 3,4:小吉 5,6,7:凶 8,9,10: 大凶
print(omikuji, end=":")

if omikuji == 1:
    print("大吉")
elif omikuji == 2:
    print("中吉")
elif omikuji  <=4:
    print("小吉")
elif omikuji  <=7:
    print("凶")
else:
    print("大凶")