import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""测试默认雇员信息和自定义雇员信息"""
	
	def setUp(self):
		"""创建一个调查对象和雇员信息"""
		self.eric = Employee('eric', 'matthes', 65000)

	def test_give_default(self):
		"""测试默认的增长工资策略是否工作"""
		self.eric.give_raise()
		self.assertEqual(self.eric.salary, 70000)

	def test_give_custom_raise(self):
		"""测试自定义的增长工资策略是否工作"""
		self.eric.give_raise(1000)
		self.assertEqual(self.eric.salary, 66000)

unittest.main()
