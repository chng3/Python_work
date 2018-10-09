#使用函数range() 创建一个列表，其中包含10个整数（即1-10）的平方
#平方用**表示

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)


#使用更加简洁的代码实现
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#对数字列表执行简单的统计计算

digits = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 0]
print(min(digits))  #打印出列表中的最小值，使用min()函数

print(max(digits))  #打印出列表中的最大值，使用max()函数

print(sum(digits))  #打印出列表数字的总和


#列表解析

#更加有效率的创建数字列表
squares = [value**2 for value in range(1,11)]   #列表名 = [表达式 for循环语句(为表达式提供值)]
print(squares)



