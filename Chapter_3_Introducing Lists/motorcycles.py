#修改，添加，删除列表元素

#修改列表元素
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#在列表中添加元素

#在末尾添加元素，使用方法append()
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#在列表中插入元素,使用方法insert()
motorcycles.insert(0,'ducati')  #在索引为0的位置插入元素
print(motorcycles)
motorcycles.insert(2,"toyota")  #在索引为2的位置插入元素
print(motorcycles)

#从列表中删除元素,使用del语句
del motorcycles[0] #删除列表中的第一个元素  
print(motorcycles)

del motorcycles[2] #删除列表中的第三个元素
print(motorcycles)

#使用方法pop()删除元素

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

popped_motorcycle = motorcycles.pop()   #把列表中最后一个元素删除，并储存起来赋值给popped_motorcycle变量
print(motorcycles)
print(popped_motorcycle)

#使用方法pop() 实例
#列出我最新购买的车是哪款摩托车
motorcycles = ["honda", "yamaha" , "suziki"]
last_owned = motorcycles.pop()
first_owned = motorcycles.pop(0) #弹(删除)出列表中的第一个元素，并将值赋值给变量first_owned.
print("The last motorcycles I owned was a " + last_owned.title() + ".")
print("The first motorcycles I owned was a " + first_owned.title() + ".")


#根据值删除元素，使用方法remove()

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles.remove('suzuki')
print(motorcycles)


#使用remove()从列表中删除元素后，可以接着使用它的值
#删除元素honda，并打印出删除他的原因

too_expensive  = "honda"    #将元素honda赋值给变量too_expensive
motorcycles.remove(too_expensive)   #删除元素honda

print(motorcycles)

print("\nA " + too_expensive.title() + " is too expensive for me.")























