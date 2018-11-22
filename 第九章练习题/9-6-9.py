# 9-6 冰激凌小店
# 9-1 餐馆

class Restaurant():
	"""用一个类来介绍餐馆"""
	
	def __init__(self, restaurant_name, cuisine_type):
		"""初始化属性restaurant_name和cuisine_type"""
		self.restaurant_name = restaurant_name.title()
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		"""显示前述两项信息"""
		msg = self.restaurant_name + " serves wonderful " + self.cuisine_type + '.'
		print("\n" + msg)
		
	def open_restaurant(self):
		"""指出餐馆正在营业"""
		msg = self.restaurant_name + " is open. Come on in!"
		print("\n" + msg)

class IceCreamStand(Restaurant):
       def __init__(self, restaurant_name, cuisine_type='ice_cream'):
              super().__init__(restaurant_name, cuisine_type)
              self.flavors = []

       def show_flavors(self):
              print("\nWe have the following flavors available:")
              for flavor in self.flavors:
                     print("- " + flavor.title())


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()



# 9-7 管理员
class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")
        
    def increment_login_attempts(self):
              """增加login_attempts的值"""
              self.login_attempts += 1

    def reset_login_attempts(self):
              """将login_atempts的值重置为0"""
              self.login_attempts = 0

        
class Admin(User):
        """具有管理权限的用户"""
        def __init__(self, first_name, last_name, username, email, location):
                """初始化管理员属性"""
                super().__init__(first_name, last_name, username, email, location)
                self.privileges = []

        def show_privileges(self):
                """显示管理员的权限"""
                print("\nPrivileges:")
                for privilege in self.privileges:
                        print("- " + privilege)

eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges = [
        'can reset passwords',
        'can moderate discussions',
        'can suspend accounts',
        ]
eric.show_privileges()





# 9-8 权限

class Privileges():
        """存储管理员权限的类"""
        def __init__(self, privileges=[]):
                self.privileges = privileges

        def show_privileges(self):
                """显示管理员的权限"""
                print("\nPrivileges:")
                if self.privileges:
                        for privilege in self.privileges:
                                print("- " + privilege)
                else:
                        print("- This user has no privileges.")

class Admin(User):
        """具有管理权限的用户"""
        def __init__(self, first_name, last_name, username, email, location):
                """初始化管理员属性"""
                super().__init__(first_name, last_name, username, email, location)
                self.privileges = Privileges()

eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges.show_privileges()

print("\nAdding privileges...")
eric_privileges = [
        'can reset passwords',
        'can moderate discussions',
        'can suspend accounts',
        ]

eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()



# 9-9 电瓶升级

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

class Battery():
       """一次模拟电动汽车电瓶的简单尝试"""

       def __init__(self, battery_size=60):
              """初始化电瓶的属性"""
              self.battery_size = battery_size

       def describe_battery(self):
               
              """打印一条描述电瓶容量的消息"""
              print("This car has a " + str(self.battery_size) + "-kWh battery.")

       def get_range(self):
               
              """打印一条消息，指出电瓶的续航里程"""
              if self.battery_size == 60:
                     range = 140
              elif self.battery_size == 85:
                     range = 185

              message = "This car can go approximately " + str(range)
              message += " miles on a full charge"
              print(message)

       def upgrade_battery(self):

              """升级电瓶容量"""
              if self.battery_size == 60:
                     self.battery_size = 85
                     print("Upgraded the battery to 85 kWh.")
              else:
                     print("The battery is already upgradeed.")
                        
              
class ElectricCar(Car):
              
       def __init__(self, make, model, year):
              """
              电动汽车的独特之处
              初始化父类的属性，再初始化电动汽车特有的属性
              """
              super().__init__(make, model, year)
              self.battery = Battery()



print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
