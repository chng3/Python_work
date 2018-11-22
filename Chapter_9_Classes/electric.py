# 9.3 继承

# 9.3.1 子类的方法__init__()

class  Car():
       """一次模拟汽车的简单尝试"""

       def __init__(self, make, model, year):
              self.make = make
              self.model = model
              self.year = year
              self.odometer_reading = 0

       def get_descriptive_name(self):
              """返回整洁的描述性信息"""
              long_name = str(self.year) + ' ' + self.make + ' ' + self.model
              return long_name.title()

       def read_odometer(self):
              """打印一条指出汽车里程的消息"""
              print("This car has " + str(self.odometer_reading) + " miles on it.")

       def update_odometer(self, mileage):# 通过方法修改属性的值
              """
              将里程表读数设置为指定的值
              禁止将里程表读数往回调
              """
              #添加逻辑，禁止任何人把里程表读数往回调
              if mileage > self.odometer_reading:
                     self.odometer_reading = mileage
              else:
                     print("You can't roll back an odometer!")

       def increment_odometer(self, miles):
              """
              将里程表读数增加指定的量
              禁止增量负数，防止有人利用它来回拨里程表
              """
              if miles >= 0:
                     self.odometer_reading += miles
              else:
                     print("You can't roll back an odometer!")


class ElectricCar(Car):
       """电动汽车的独特之处"""
       def __init__(self, make, model, year):
              """初始化父类的属性"""
              super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# 9.3.3 给子类定义属性和方法

class ElectricCar(Car):
              
       def __init__(self, make, model, year):
              """
              电动汽车的独特之处
              初始化父类的属性，再初始化电动汽车特有的属性
              """
              super().__init__(make, model, year)
              self.battery_size = 70

       def describe_battery(self):
              """打印一条描述电瓶车容量的消息"""
              print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# 9.3.4 重写父类的方法
class ElectricCar(Car):
       def fill_gas_tank(self):
              """电动汽车没有油箱"""
              print("This car doesn't need a gas tank!")

# 9.3.5 将实例用作属性

class Battery():
       """一次模拟电动汽车电瓶的简单尝试"""

       def __init__(self, battery_size=70):
              """初始化电瓶的属性"""
              self.battery_size = battery_size

       def describe_battery(self):
              """打印一条描述电瓶容量的消息"""
              print("This car has a " + str(self.battery_size) + "-kWh battery.")

       def get_range(self):
              """打印一条消息，指出电瓶的续航里程"""
              if self.battery_size == 70:
                     range = 240
              elif self.battery_size == 85:
                     range = 270

              message = "This car can go approximately " + str(range)
              message += " miles on a full charge"
              print(message)
              
class ElectricCar(Car):
              
       def __init__(self, make, model, year):
              """
              电动汽车的独特之处
              初始化父类的属性，再初始化电动汽车特有的属性
              """
              super().__init__(make, model, year)
              self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

my_tesla.battery.get_range()



