#5-8 以特殊方式跟管理员打招呼

user_names = ['eric', 'admin', 'melo',
               'harden', 'paul']

for user_name in user_names:
    if user_name == 'admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print("Hello " + user_name.title() + ",thank you for logging in again")

print("\n")

#5-9 处理没有用户的情形
user_names = ['eric', 'admin', 'melo',
               'harden', 'paul']
#清空列表元素
user_names.remove('eric')
user_names.remove('melo')
user_names.remove('admin')
user_names.remove('harden')
user_names.remove('paul')

if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello " + user_name.title() + ",thank you for logging in again")
else:
    print("We need to find some users!")


#检查用户名


current_users = ['eric', 'admin', 'melo',
               'harden', 'paul']
new_users = ['ERIC', 'paul', 'unboxing',
             'therapy', 'jason']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("你需要输入别的用户名")
    else:
        print("这个用户名未被使用")



#5-11 序数

numbers = [1, 2, 3, 4, 5,
           6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")

