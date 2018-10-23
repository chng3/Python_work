# 词汇表2


词汇表 = {'亵渎': '轻慢； 不敬',
       '拨冗': '推开繁忙的工作，抽出时间',
       '贸然': '轻率的样子。指遇事不经深思熟虑,随便就决定做法',
       '风姿绰约': '形容人的風采姿容非常優美。',
       '北平': '北京旧称',
       }

for vocabulary_name, meaning in 词汇表.items():
    print(vocabulary_name + ":" + meaning)

# 6-5 河流

rives = {
    'Rhein': 'Germany',
    'nile': 'egypt',
    'Donau': 'Austria',
    }

for river_name, country in rives.items():   
    print("The " + river_name.title() + " runs through " + country.title() + '.')

for river_name in rives.keys():
    print(river_name.title())

for country in rives.values():
    print(country.title())



print("\n")

# 6-6 调查

favorite_languages = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'Python'
    }

people = ['kevin', 'edward', 'phil']

for name in people:
    if name in favorite_languages.keys():
        print("Thanks, " + name.title())
    else:
        print(name.title() + " ,Can you accept our investigation?")















