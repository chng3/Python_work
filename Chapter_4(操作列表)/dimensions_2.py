#遍历元组中的所有值

dimensions = (200, 50)
for dimension in dimensions:    #像列表一样，使用for循环来遍历元组中的所有值
    print(dimension)


#修改元组变量
#虽然元组元素比可以直接修改，但可以重新定义整个元组

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100) #重新定义元组
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


