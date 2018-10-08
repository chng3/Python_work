#组织列表

#使用方法sort()永久性的修改列表的排列顺序

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()     #按字母顺序排列
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse = True)   #按与字母顺序相反的顺序排列，向sort()方法传递参数reverse = True
print(cars)


#使用函数sorted()对列表进行临时排序


cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))     #按字母顺序临时显示该列表，使用函数sorted()

print("\nHere is the original list again:")
print(cars)
print("\n")

print(sorted(cars, reverse = True))  #按字母顺序相反顺序临时显示该列表，使用函数sorted(列表名,reverse = True),传递参数 reverse = True.
print("\nHere is the original list again:")
print(cars)
print("\n")
#倒着打印列表
#使用方法reverse()

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)     #方法reverse()永久性地修改列表元素的排列顺序，反转列表元素的排列顺序
cars.reverse()
print(cars)     #再次使用方法reverse()，可以恢复到原来的排列顺序

#确定列表的长度

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))       #使用函数len()可快速获悉列表的长度


