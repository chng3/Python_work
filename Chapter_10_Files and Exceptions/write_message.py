# 10.2 写入文件

# 10.2.1 写入空文件

filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.")

# 10.2.2 写入多行
with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")

# 10.2.3 附加到文件

with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datesets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")
	
