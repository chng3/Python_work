#4-10
my_foods = ['pizza', 'falafel', 'carrot cake', 'chocolate']
print("The first three items in the list are:")
print(my_foods[:3])

print("Three items from the middle of the list are:")
print(my_foods[1:3])

print("The last items in the list are:")
print(my_foods[-3:])


#4-11 你的披萨和我的披萨

pizzas = ['tomato', 'banana', 'apple']
friend_pizzas = pizzas[:]

pizzas.append('hotdog')

friend_pizzas.append('pineapple')

print("My favorite pizzas are:")
for pizza in pizzas[:]:
    print(pizza)

print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas[:]:
    print(friend_pizza)



#4-12
foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']
for food in foods[:]:
    print(food)
