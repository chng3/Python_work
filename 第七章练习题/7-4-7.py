# 7-4 比萨配料

prompt = "\n请输入您要的配料："
prompt += "\n(输入quit退出)"

active = True
while active:
       add = input(prompt)
       if add == 'quit':
              break
       else:
              print("我们会在比萨中添加：" + add)


# 7-5 电影票

prompt = "How old are you? "

while True:
       age = input(prompt)
       age = int(age)
       if age < 3:
              print("You are for free!")
              break
       elif age <= 12:
              price = '10 dollar'
       else:
              price = '15 dollar'
       print("You need to spend " + price + " to get tickets.")
       break

# 7-6 三个出口

prompt = "\n请输入您要的配料："
prompt += "\n(输入quit退出)"

active = True
while active:
       add = input(prompt)
       if add == 'quit':
              break
       else:
              print("我们会在比萨中添加：" + add)
              active = False

# 7-7 无限循环
a = 12
while a < 4:
       a += 1
       print(a)
