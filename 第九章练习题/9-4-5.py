# 9-4 就餐人数

class Restaurant():
       """用一个类来介绍餐馆"""
       def __init__(self, restaurant_name, cuisine_type):
              """初始化属性restaurant_name和cuisine_type"""
              self.restaurant_name = restaurant_name.title()
              self.cuisine_type = cuisine_type
              self.number_served = 0	#添加属性
              
       def describe_restaurant(self):
              """显示前述两项信息"""
              msg = self.restaurant_name + " serves wonderful " + self.cuisine_type + '.'
              print("\n" + msg)
		
       def open_restaurant(self):
              """指出餐馆正在营业"""
              msg = self.restaurant_name + " is open. Come on in!"
              print("\n" + msg)

       def set_number_served(self, number_served):
              """设置就餐人数"""
              self.number_served = number_served
               
       def increment_number_served(self, additional_served):
              """允许用户将就餐人数增加"""
              self.number_served += additional_served
       
restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 430
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(1257)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(239)
print("Number served: " + str(restaurant.number_served))


# 9-5 尝试登录次数
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



eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print("  Login attempts: " + str(eric.login_attempts))

print("Resetting login attempts...")
eric.reset_login_attempts()
print("  Login attempts: " + str(eric.login_attempts))
