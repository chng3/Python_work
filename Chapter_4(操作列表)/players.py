#使用列表的一部分

#切片

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3])     #打印列表中的前三个元素

print(players[1:4])     #打印列表中第2-4个元素

print(players[:4])      #从列表开头开始提取，打印前四个元素

print(players[2:])      #提取从第三个元素到列表末尾的所有元素

print(players[-3:])     #输入名单上的最后三名队员


#遍历切片
print("Here are the first three players on my team:")
for player in players[:3]:      #遍历前三名队员
    print(player.title())       #打印前三名队员






