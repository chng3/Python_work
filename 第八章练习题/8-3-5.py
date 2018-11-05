# 8-3 T恤

def make_shirt(size, message):
       """Summarize the shirt that's going to be made."""
       print("\nI'm going to make a " + size + " t-shirt.")
       print('It will say, "' + message + '"')

make_shirt('large', 'I love Python!')
make_shirt(message='Readability counts', size='medium')

# 8-4 大号T恤

def make_shirt(size='large', message='I love Python!'):
       """Summarize the shirt that's going to be made."""
       print("\nI'm going to make a " + size + " t-shirt.")
       print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')

# 8-5 城市

def describe_city(city, country='chile'):
       """描述国家"""
       msg = city.title() + " is in " + country.title() + '.'
       print(msg)

describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')
