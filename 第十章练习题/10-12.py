# 10-12 记住喜欢的数字
import json

def get_stored_number():
	"""如果存贮了数字，就获取它"""
	filename = 'user_favorite_number.json'
	
	try:
		with open(filename) as f:
			number = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return number

def get_new_number():
	"""提取新的用户喜欢的数字，并将其存储到文件中"""
	filename = 'user_favorite_number.json'
	
	number = input("What is your favorite number? ")
	with open(filename, 'w') as f:
		json.dump(number, f)
	return number
		
def user_number():
	"""记住喜欢的名字"""
	number = get_stored_number()
	if number:
		print("haha! I know your favorite number! It's " + number + ".")
	else:
		number = get_new_number()
		print("I know your favorite number! It's " + number + ".")

user_number()
	
	
