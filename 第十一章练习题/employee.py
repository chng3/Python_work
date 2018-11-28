# 11-3 雇员

class Employee():
	"""管理雇员信息"""
	
	def __init__(self,f_name, l_name, salary):
		"""初始化属性"""
		self.f_name = f_name.title()
		self.l_name = l_name.title()
		self.salary = salary
	
	def give_raise(self, amount=5000):
		"""年薪增加5000美元"""
		self.salary += amount


