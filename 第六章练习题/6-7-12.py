# coding:utf-8
# 6-7 人

小猪佩奇 = {'first_name': 'pig', 'last_name': 'small', 'age': 23, 'city': 'beijing'}
陈奕迅 = {'first_name': 'eason', 'last_name': 'chan', 'age': 44, 'city': 'hongkong'}
陈冠希 = {'first_name': 'edison', 'last_name': 'chen', 'age': 38, 'city': 'los angeles'}

people = [小猪佩奇, 陈奕迅, 陈冠希]

for stars in people:
    print(str(stars) + "\n")


# 6-8 宠物

tiedy = {'type': 'dog', 'master': 'paul'}
coddy = {'type': 'cat', 'master': 'lebron'}
katie = {'type': 'fish', 'master': 'kobe'}

pets = [tiedy, coddy, katie]

for pet in pets:
    print(str(pet) + "\n")



# 6-9 喜欢的地方

favorite_places = {
    'kobe': ['los angeles', 'beijing', 'shenzhen'],
    'lebron': ['miami', 'cleveland', 'newyork'],
    'kevin': [ 'oklahoma', 'newyork', 'los angeles']
    }

for name, locations in favorite_places.items():
    print(name.title() + " favorite places are:")
    for location in locations:
        print("\t" + location.title())



# 6-10 喜欢的数字

favorite_numbers = {
    'kevin': [3, 89],
    'harden': [2, 77],
    'rookie': [4, 67],
    'curry': [88, 44],
    'hardwood': [89, 59]
    }


for name, numbers in favorite_numbers.items():
    print(name.title() + " favorite number are:")
    for number in numbers:
        print("\t\t\t  " + str(number))




# 6-11 城市

cities = {
    
    'los angeles':{
    'country': 'usa',
    'population': "199k",
    'fact': 'top1 city in the world'
        },
    
    'shenzhen':{
    'country': 'china',
    'population': "133k",
    'fact': 'top1 city in china'
        },

    'guanzhou':{
    'country': 'china',
    'population': "111k",
    'fact': 'top1 city in china'
        },

    }

for city_name, city_info in cities.items():
    print("\nCity_name: " + city_name)
    population = city_info['population']
    country = city_info['country']
    print("\t Country: " + country)
    print("\t Population: " + population)
    print("\t Fact: " + city_info['fact'])






