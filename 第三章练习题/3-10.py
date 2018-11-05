#3-8

destination = ['houston', 'seattle', 'tokyo', 'paris', 'xiamen']
print('Here is the original list:')
print(destination)

print(sorted(destination))    #按字母顺序打印这个列表，但并不修改列表

print(destination)      

print(sorted(destination, reverse = True))  #按字母相反顺序打印这个列表，但并不修改列表

print(destination)

destination.reverse()       #按元素的相反方向，修改元素的排列顺序
print(destination)

destination.reverse()   #恢复元素原始的排列顺序
print(destination)

destination.sort()  #使元素按字母顺序排列
print(destination)

destination.sort(reverse = True)    #使元素按字母顺序相反的顺序排列
print(destination)

#3-9

guest = ["Kevin", "Melo", "Harden"]

print("I invite "+ str(len(guest)) + " people to have dinner with me.")

#3-10
#修改
nation = ['korea', 'china', 'japan', 'british']
print(nation)
nation[0] = 'india'
print(nation)

#添加
nation = ['korea', 'china', 'japan', 'british']
print(nation)
nation.append('india')
print(nation)

#插入
nation = ['korea', 'china', 'japan', 'british']
print(nation)
nation.insert(2,'india')
print(nation)

#删除
nation = ['korea', 'china', 'japan', 'british']
print(nation)
del nation[0]
del nation[2]
print(nation)

#使用弹出删除并利用
nation = ['korea', 'china', 'japan', 'british']
print(nation)
popped_nation = nation.pop()    #弹出列表最后一个并利用
print(nation)
print("I like " + popped_nation + '.')
nation = ['korea', 'china', 'japan', 'british']
print(nation)
popped_nation = nation.pop(2)   #弹出列表元素第三个
print(nation)
print("I like " + popped_nation + '.')

#根据值删除元素
nation = ['korea', 'china', 'japan', 'british']
print(nation)
nation.remove('china')
print(nation)

#组织列表

nation = ['korea', 'china', 'japan', 'british']
print(nation)
nation.sort()   #按字母顺序排序
print(nation)

nation.sort(reverse = True)
print(nation)   #按字母相反顺序排序

#临时排序
nation = ['korea', 'china', 'japan', 'british']
print(nation)
print(sorted(nation))   #临时按字母顺序排序
print(nation)   #验证


print(sorted(nation,reverse = True))    #临时按字母相反顺序排序

print(nation)   #验证


#倒着打印
nation = ['korea', 'china', 'japan', 'british']
print(nation)
nation.reverse()    #列表元素倒着排列
print(nation)   
nation.reverse()
print(nation)   #恢复

#确认列表长度
print(len(nation))














