# 10-8 猫和狗
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
	print("\nReading file: " + filename)
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
			print(contents)
	except FileNotFoundError:
		print("  Sorry, I can't find that file.")
