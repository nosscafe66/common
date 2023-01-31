count = int(input())

for i in range(count):
    number = int(input())
    print(number)
    
    if number == 10:
        print(str(number) + "は10に等しい")
    elif number > 10:
        print(str(number) + "は10より大きい")
    else:
        print(str(number) + "は10未満")