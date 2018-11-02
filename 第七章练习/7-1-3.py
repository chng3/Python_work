# 7-1 汽车租赁

car_name = input("What car do you want? ")

print("Let me see if I can find you a " + car_name + ".")


# 7-2 餐馆订位

number = input("一共有多少人用餐？")
number = int(number)

if number > 8:
    print("没有空桌")
else:
    print("有空桌")


# 7-3 10的整数倍
number = input("请输入数字: ")

if int(number) % 10:
    print("该数字不是10的整数倍。")
else:
    print("该数字是10的整数倍。")
