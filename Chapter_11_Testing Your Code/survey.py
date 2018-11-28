# 11.2 测试类

# 11.2.1 各种断言方法

# 11.2.2 一个要测试的类

class AnonymousSurvey():
	"""收集匿名调查问卷的答案"""

	def __init__(self, question):
		self.question = question
		self.responses = []

	def show_question(self):
		"""显示调查问卷"""
		print(self.question)
	
	def store_response(self, new_response):
		"""储存单份调查问卷"""
		self.responses.append(new_response)
		
	def show_result(self):
		"""显示收集到的所有答卷"""
		print("Survey results:")
		for response in self.responses:
			print('- ' + response)


