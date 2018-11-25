# 10-9 沉默的猫和狗

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
	
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
			
	except FileNotFoundError:
		pass

	else:
		print("\nReading file: " + filename)
		print(contents)
