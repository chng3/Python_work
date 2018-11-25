# 10.3 异常

# 10.3.1 处理ZeroDivisionError 异常

# print(5/0)

# 10.3.2 使用try_except 代码块
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")
	

# 10.3.3 使用异常避免崩溃

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	# 10.3.4 else代码块
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)
		




