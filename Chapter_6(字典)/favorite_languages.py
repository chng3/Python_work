#由类似对象组成的字典

favorite_languages = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'Python'
    }

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

#遍历字典


for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")


#遍历字典中的所有键
#使用方法keys()

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']     

for name in favorite_languages:
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite languages is " +
              favorite_languages[name].title() + "!")



#使用keys()确定某个人是否接受了调查

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")




#按(字母)顺序遍历字典中的所有键


for name in sorted(favorite_languages.keys()):
    print(name.title() + ",thank you for taking the poll.")


#遍历字典中的所有值
print("The following languages have been mentioned:")

for language in favorite_languages.values():
    print(language.title())


#剔除重复项，使用集合(set)
print("\n")
for language in set(favorite_languages.values()):
    print(language.title())











































