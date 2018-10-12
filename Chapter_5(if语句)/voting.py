#5.3 if语句

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

#if-else语句
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please registered to vote as soon as you turn 18!")

#if-elif-else语句
#根据年龄段收费的游乐场
age = 12

if age < 4:
    print("You admission cost is $0.")
elif age < 18:
    print("You admission cost is $5.")
else:
    print("You admission cost is $10.")


