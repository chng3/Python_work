# 8-9 魔术师

def show_magicians(magicians):
       """打印列表中每个魔术师的名字"""
       for magician in magicians:
              print(magician.title())
              
magicians = ['刘谦', 'harry houdini', 'david blaine', 'teller']
show_magicians(magicians)

# 8-10 了不起的魔术师

def show_magicians(magicians):
       """打印列表中每个魔术师的名字"""
       for magician in magicians:
              print(magician.title())

def make_great(magicians):
       """让每个魔术师都很棒，并将它加入到伟大的魔术师身上"""
       # 创建一个新的列表来存放修改后的魔术师名单
       great_magicians = []

       # 让每一名魔术师的名字后都添加字样the great，并将每一个都添加到新的列表当中
       while magicians:
              magician = magicians.pop()
              great_magician = magician + ' the Great'
              great_magicians.append(great_magician)

       # 遍历新的列表，并将每一项都弹出放置到原本存放魔术师的列表(已空)当中
       for great_magician in great_magicians:
              magicians.append(great_magician)


magicians = ['刘谦', 'harry houdini', 'david blaine', 'teller']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)


# 8-11 不变的魔术师

def show_magicians(magicians):
       """打印列表中每个魔术师的名字"""
       for magician in magicians:
              print(magician.title())

def make_great(magicians):
       """让每个魔术师都很棒，并将它加入到伟大的魔术师身上"""
       # 创建一个新的列表来存放修改后的魔术师名单
       great_magicians = []

       # 让每一名魔术师的名字后都添加字样the great，并将每一个都添加到新的列表当中
       while magicians:
              magician = magicians.pop()
              great_magician = magician + ' the Great'
              great_magicians.append(great_magician)

       # 遍历新的列表，并将每一项都弹出放置到原本存放魔术师的列表(已空)当中
       for great_magician in great_magicians:
              magicians.append(great_magician)
              
       return magicians

magicians = ['刘谦', 'harry houdini', 'david blaine', 'teller']
show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians)

