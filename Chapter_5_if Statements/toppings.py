#检查是否不相等

#判断两个值不相等时使用惊叹号和等号（!=）

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':    #判断requested_topping的值是不是 不是‘anchovies’
    print("Hold the anchovies!")        #不是的话 则打印消息Hold the anchovies!


#测试多个条件

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")

print("\nFinished making your pizza!")

print("\n")


#检查特殊元素

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':    #检查顾客点的是否是青椒，如果是，则显示出一条消息，指出不能点青椒的原因
        print("Sorry,we are out of green peppers right now.")
    else:       #确保其他配料都添加到此披萨
        print("Adding " + requested_topping + ".")      

print("\nFinished making your pizza!")

print("\n")


#确定列表不是空的

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


print("\n")


#使用多个列表

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'frech fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")



