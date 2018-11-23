# 9.4 导入类

# 9.4.1 导入单个类

from car1 import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 9.4.3 从一个模块中导入多个类

from car1 import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

# 9.4.4 导入整个模块

import car1

my_beetle = car1.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car1.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

# 9.4.5 导入模块中的所有类

# from module_name import *




