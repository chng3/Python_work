#创建数值列表

#使用函数range()

for value in range(1,5):
    print(value)

#使用range()创建数字列表
number = list(range(1,6))
print(number)


#使用函数range(),指定步长

even_number = list(range(2,11,2))   #打印1到10内的偶数,指定步长为2
print(even_number)
