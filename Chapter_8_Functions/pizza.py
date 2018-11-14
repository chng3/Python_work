# 8.5 传递任意数量的实参

def make_pizza(*toppings):
       """打印顾客点的所有配料"""
       print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 添加循环

def make_pizza(*toppings):
       """概述要制作的披萨"""
       print("\nMaking a pizza with the following toppings:")
       for topping in toppings:
              print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')

# 8.5.1 结合使用位置实参和任意数量实参

def make_pizza(size, *toppings):
       """概述要制作的比萨"""
       print("\nMaking a " + str(size) +
             "-inch pizza with the following toppings:")
       for topping in toppings:
              print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')



