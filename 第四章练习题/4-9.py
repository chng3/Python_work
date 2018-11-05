#4-9练习
#4-3
for value in range(1,21):
    print(value)


#4-6
values = []
for value in range(1,21,2):
    values.append(value)
print(values)

#4-7
for value in range(3,31,3):
    print(value)

#4-8
cubes = []
for cube in range(1,11):
    cubes.append(cube**3)
print(cubes)

#4-9
#使用列表解析
cubes = [cube**3 for cube in range(1,11)]
print(cubes)
