# Chapter_10 文件和异常

# 10.1 从文件中读取数据

# 10.1.1 读取整个文件

with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())
	

# 10.1.2 文件路径

# 相对路径
file_path = 'text_files/pi_digits.txt'
with open(file_path) as file_object:
	contents = file_object.read()
	print(contents.rstrip())

# 绝对路径
file_path = '/home/chngdolphin/Desktop/Github/Python_work/Chapter_10_Files and Exceptions/pi_digits.txt'
with open(file_path) as file_object:
	contents = file_object.read()
	print(contents.rstrip())
	

# 逐行读取

filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())
		
		
# 10.1.4 创建一个包含文件各行内容的列表

with open(filename) as file_object:
	lines = file_object.readlines()
	
for line in lines:
	print(line.rstrip())
	



