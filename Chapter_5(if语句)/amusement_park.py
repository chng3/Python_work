#if-elif-else语句
#根据年龄段收费的游乐场

age = 12

if age < 4:
    print("You admission cost is $0.")
elif age < 18:
    print("You admission cost is $5.")
else:
    print("You admission cost is $10.")



#为了让代码更加简洁，不在if-elif-else语句中打印价格，而只在其中设置门票价格

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + '.')


#使用多个elif代码块

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + '.')


#省略else代码块

age = 34

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:     #在顾客的年龄超过65（含）时，将价格设置为5美元，这比使用else代码块更清晰些。相较于else语句，则是一条包罗万象的语句。
    price = 5

print("Your admission cost is $" + str(price) + '.')

