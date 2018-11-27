# 从user_favorite_number.json文件中读取值
import json

filename = 'user_favorite_number.json'

with open(filename) as f:
	number = json.load(f)
	print("I know your favorite number! It's " + number + ".")
