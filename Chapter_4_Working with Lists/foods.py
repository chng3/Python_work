#复制列表

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]      #从my_foods列表中提取了切片，从而创建这个列表的副本

friend_foods.append('cannoli')
my_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite food are:")
print(friend_foods)



