# 5-3 外星人颜色1

#第一个版本

alien_color = 'green'

if alien_color == 'green':
    print("玩家获得5个点")

#第二个版本
if alien_color == 'red':
    print("")

# 5-4外星人颜色2
 
# 第一个版本
    
alien_color = 'green'

if alien_color == 'green':
    print("你因射杀该外星人获得了5个点")
else:
    print("你获得10个点")

# 第二个版本

alien_color = 'red'

if alien_color == 'green':
    print("你因射杀该外星人获得了5个点")
else:
    print("你获得10个点")


# 5-5外星人颜色3

# 版本一
alien_color = 'green'

if alien_color == 'green':
    print("你获得了5个点")
elif alien_color == 'yellow':
    print("你获得了10个点")
else:
    print("你获得了15个点")

# 版本二
alien_color = 'yellow'

if alien_color == 'green':
    print("你获得了5个点")
elif alien_color == 'yellow':
    print("你获得了10个点")
else:
    print("你获得了15个点")

# 版本三

alien_color = 'red'

if alien_color == 'green':
    print("你获得了5个点")
elif alien_color == 'yellow':
    print("你获得了10个点")
else:
    print("你获得了15个点")


#5-6 人生的不同阶段

age = 21

if age < 2:
    print("你是婴儿")
elif age < 4:
    print("你正蹒跚学步")
elif age < 13:
    print("你是儿童")
elif age < 20:
    print("你是青少年")
elif age < 65:
    print("你是成年人")
else:
    print("你是老年人")

# 5-7 喜欢的水果

favorite_fruits = ['apple', 'pineapple', 'pear']

if 'apple' in favorite_fruits:
    print("You really like apple!")
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'blueberry' in favorite_fruits:
    print("You really like blueberry!")
if 'pear' in favorite_fruits:
    print("You really like pear!")
if 'pineapple' in favorite_fruits:
    print("You really like pineapple!")
