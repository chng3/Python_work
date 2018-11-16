
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
		
restaurant = Restaurant('the mean queen', 'pizza')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2 三家餐馆

restaurant_1 = Restaurant('the mean queen', 'pizza')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant("ludvig's bistro", 'seafood')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('mango thai', 'thai food')
restaurant_3.describe_restaurant()

# 9-3 用户

class User():
	"""模拟描述用户信息"""
	
	def __init__(self, first_name, last_name, username, email, location):
		"""用户简介"""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.username = username
		self.email = email
		self.location = location.title()
		
	def describe_user(self):
		"""打印用户信息摘要"""
		print("\n" + self.first_name + " " +self.last_name)
		print(" Username: " + self.username)
		print(" Email: " + self.email)
		print(" Location: " + self.location)
		
	def greet_user(self):
		"""发出个性化的问候"""
		print("\nWelcome back, " + self.username + "!")
		
eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()
