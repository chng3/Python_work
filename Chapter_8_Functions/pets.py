# 8.2 传递实参
# 8.2.1 位置实参

def describe_pet(animal_type, pet_name):
       """显示宠物的信息"""
       print("\nI have a " + animal_type + ".")
       print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("hamster", "harry")
# 调用函数多次
describe_pet('dog', 'willie')


# 8.2.2 关键字实参

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


# 8.2.3 默认值

def describe_pet(pet_name, animal_type='dog'):
       """显示宠物的信息"""
       print("\nI have a " + animal_type + ".")
       print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('willie')
describe_pet(pet_name="willie")
describe_pet(pet_name="willie", animal_type='cat')


describe_pet(pet_name="harry", animal_type='hamster')


# 8.2.4 等效的函数调用

# 一条名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')

# 一条名为Harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')






# 避免实参错误
def describe_pet(animal_type, pet_name):
       """显示宠物的信息"""
       print("\nI have a " + animal_type + ".")
       print("My " + animal_type + "'s name is " + pet_name.title() + ".")
       
describe_pet()


