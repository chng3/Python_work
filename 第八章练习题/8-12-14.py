# 8-12 三明治

def make_sandwich(*items):
       """概述顾客点的三明治中添加的食材"""
       print("\nI'll make you a great sandwich:")
       for item in items:
              print("  ...adding " + item + " to your sandwich.")
       print("Your sandwich is ready!")

make_sandwich('roast beef', 'cheddar cheese', 'lettuce',)
make_sandwich('turkey', 'apple shices', 'honey mustard',)
make_sandwich('peanut butter', 'strawberry jam')

# 8-13 用户简介

def build_profile(first, last, **user_info):
       """创建一个字典，其中包含我们知道的有关用户的一切"""
       profile = {}
       profile['first_name'] = first
       profile['last_name'] = last
       for key, value in user_info.items():
              profile[key] = value
       return profile
user_profile = build_profile('chng', 'dolphin',
                             location='guangzhou',
                             field='software',
                             nationality='han')
print(user_profile)



# 8-14 汽车

def make_car(manufacturer, model, **options):
       """存储汽车信息的字典"""
       car_dict = {
              'manufacturer': manufacturer.title(),
              'model': model.title(),
              }
       for key, value in options.items():
              car_dict[key] = value
              
       return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_accord = make_car('honda', 'accord', year=1991, color='white',
                     headlights='popup')
print(my_accord)
       
