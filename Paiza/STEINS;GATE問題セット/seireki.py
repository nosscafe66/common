# coding: utf-8
# 西暦年から平成年を求める
import datetime

seireki = datetime.date.today().year
print("西暦"+str(seireki) + "年は、", end="")

# 平成1年は西暦1989年。その差は1988

heisei = seireki -1988
print("平成"+str(heisei)+"年です。")


# 西暦を令和年に変換
import random
ad_year = random.randint(2019, 2099) #西暦年
print("西暦" + str(ad_year) + "年は", end = "")

# 令和年を計算
era_year = ad_year - 2018
# 令和年を出力
print("令和" + str(era_year) + "年です")