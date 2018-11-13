# 8-6 城市名

def get_city_country(city_name, country_name):
       """描述城市名字及其所属国家"""
       c_country = city_name + ', ' + country_name
       return c_country.title()

c_country1 = get_city_country('santiage', 'chile')
c_country2 = get_city_country('guangzhou', 'china')
c_country3 = get_city_country('paris', 'france')
print(c_country1)
print(c_country2)
print(c_country3)
       

# 8-7 专辑

def make_album(artist, title):
       """创建一个描述音乐专辑的字典"""
       album_dict = {
              'artist': artist.title(),
              'title': title.title(),     
              }
       return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)

# 带歌曲数
def make_album(artist, title, tracks=0):
       """创建一个描述音乐专辑的字典"""
       album_dict = {
              'artist': artist.title(),
              'title': title.title(),
              }
       if tracks:
              album_dict['tracks'] = tracks
       return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)

album = make_album('iron maiden', 'piece of mind', tracks=8)
print(album)

# 8-8 用户的专辑

def make_album(artist, title, tracks=0):
       """创建一个描述音乐专辑的字典"""
       album_dict = {
              'artist': artist.title(),
              'title': title.title(),
              }
       if tracks:
              album_dict['tracks'] = tracks
       return album_dict

# 让用户知道怎样可以退出
print("Enter 'quit' at any time to quit.")

while True:
       artist = input("\nWho's the artist?")
       if artist == 'quit':
              break
       
       title = input("What album are you thinking of?")
       if title == 'quit':
              break

       album = make_album(artist, title)
       print(album)

print("\nThanks for responding!")





       
