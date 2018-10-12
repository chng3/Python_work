# Chapter 5 if语句


cars = ['audi' , 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':    #检查当前的汽车名字是否是'bmw',如果是，就以全大写的方式打印它；
        print(car.upper())
    else:               #否者就以首字母大写的方式打印
        print(car.title())


