# 2.3字符串

#使用方法来修改字符串的大小写
name = "ada lovelace"
print(name.title())  #title()让变量name执行方法title()代表的以首字母大写的方式显示每个单词

print(name.upper()) #upper()将字符串改为全部大写
print(name.lower()) #lower()将字符串改为全部小写

#合并字符串
first_name = "ada"  
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")

#使用拼接创建消息，再把整条消息都存储在一个变量中(message)： 
message = "Hello, " + full_name.title() + "!"
print(message)

#使用制表符或换行符来添加空白
print("Python")

print("\tPython")   #使用字符组合"\t"，添加制表符

print("Python\nC")  #使用字符组合"\n",添加换行符

print("Language:\n\tPython\n\tC\n\tJavaScript") #同时包括换行符和制表符

#2.3.4删除空白
#使用rstrip()删除字符串末尾空白

#使用lstrip()删除字符串前端的空白

#使用strip()删除字符串两端的空白
favorite_language = 'python '
print(favorite_language)

favorite_language.rstrip()

print(favorite_language)

#永久删除这个字符串的空白，必须将删除操作的结果存回变量中：
favorite_language = favorite_language.rstrip()
print(favorite_language)

