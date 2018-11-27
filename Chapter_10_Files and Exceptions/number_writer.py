# 10.4 存储数据

# 10.4.1 使用json.dump() 和 json.load()

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)


