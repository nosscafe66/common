#  複数のデータ受け取り

count = int(input()) # countで指定した数字分処理が実行される

for i in range(count):
    name = input() # countで指定した数字分の入力が必要（数字の2を指定したら2個の引数が必要になるイメージ）
    print("Hello " + name)