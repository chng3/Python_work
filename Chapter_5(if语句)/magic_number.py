#比较数字

answer = 17

if answer != 42:
    print("That is not the corret answer. Please try again!")

#条件语句中可包含数学比较，如小于、小于等于、大于、大于等于：

age = 17
print(age < 19)

print(age <= 15)

print(age >15)

print(age >=15)

#检查多个条件

#使用and检查多个条件

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >21)    #检查两个人是否都不小于21岁

age_1 = 22
print(age_0 >= 21 and age_1 >=21)

#使用or检查多个条件

age_0 = 22
age_1 = 18

print(age_0 >= 21 or age_1 >=21)    #检查是否有一个满足条件，如有，则返回"True"

age_0 = 18
print(age_0 >= 21 or age_1 >=21)


#检查特定值是否包含在列表中,使用关键字 in

requested_toppings = ['mushrooms', 'onins', 'pineapple']

print('mushrooms' in requested_toppings)    #检查'mushrooms'是否在列表中，有则返回 True,没有则返回false

print('pepperoni' in requested_toppings)    #检查'pepperoni'是否在列表中，有则返回 True,没有则返回false


