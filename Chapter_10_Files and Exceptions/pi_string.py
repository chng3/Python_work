# 10.1.5 使用文件的内容

filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
	
pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# 10.1.6 包含一百万位的大型文件

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
	
pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# 10.1.7 圆周率值中包含你的生日号码吗

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
	
pi_string = ''
for line in lines:
	pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("You birthday appears in the first million digits of pi!")
else:
	print("You birthday does not appear in the first million digits of pi!")
	

