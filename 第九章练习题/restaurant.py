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
