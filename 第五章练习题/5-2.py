#5-1 条件测试

myday = 'Thursday'
print("Is mayday == 'Thursday'? I predict True.")
print(myday == 'Thursday')

print("\nIs myday == 'Sunday'? I predict False.")
print(myday == 'Sunday')
print("\n")

#5-2


year_0 = 12
year_1 = 13
print(year_0 == year_1)
print(year_0 != year_1)
print(year_0 > year_1)
print(year_0 < year_1)
print(year_0 <= year_1)
print(year_0 >= year_1)

print("\n")

name = 'James'
print(name.lower() == 'james')

print("\n")

year_0 = 18
year_1 = 22
print(year_0 <=22 and year_1 <=22)

year_0 = 25
print(year_0 <=21 or year_1 <=21)



numbers = [12, 34, 44, 44]
number_0 = 22
number_1 = 12
if number_1 in numbers:
    print("True")
if number_0 not in numbers:
    print("True")
