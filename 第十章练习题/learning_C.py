# 10-2 C语言学习笔记

filename = 'learning_python.txt'

with open(filename) as f:
	contents = f.read().replace('Python', 'C')
	print(contents)
