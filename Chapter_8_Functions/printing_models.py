import print_function

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron', 'mi5']
completed_models = []

print_function.print_models(unprinted_designs, completed_models)
print_function.show_completed_models(completed_models)

# 8.4.2 禁止函数修改列表

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron', 'mi5']

# 切片表示法[:]创建列表的副本 function_name(list_name[:])

print_function.print_models(unprinted_designs[:], completed_models)
