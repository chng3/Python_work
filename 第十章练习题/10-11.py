# 10-10 喜欢的数字
import json

favorite_number = input("What is your favorite number? ")

filename = 'user_favorite_number.json'
with open(filename, 'w') as f:
	json.dump(favorite_number, f)
