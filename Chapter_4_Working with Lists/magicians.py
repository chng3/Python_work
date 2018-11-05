#4操作列表
#使用for循环打印魔术师名单中的所有名字
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#在for循环中执行更多的操作
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ', that was a great trick!')
    print("I can't wait to see your next trick, " + magician.title() + '.\n')
print('Thank you, everyone. That was a great magic show!')
