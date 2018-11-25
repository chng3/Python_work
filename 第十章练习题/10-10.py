def count_words(filename):
	"""计算具体单词在文件中出现多少次"""
	try:
		with open(filename) as obj:
			contents = obj.read()
	except FileNotFoundError:
		pass
	else:
		"""计算单词'the'在文件中出现多少次"""
		print("\nReading file: " + filename)
		time = contents.lower().count('the')
		print("The word of the appears " + str(time) + " times!")
		
filenames = ['Tarr.txt', 'the fall of man.txt', 'Wanderings in Corsica.txt']
for filename in filenames:
	count_words(filename)
		
		
