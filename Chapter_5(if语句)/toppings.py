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
