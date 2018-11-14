# 8.4 传递列表
import greet_user2

usernames = ['hannah', 'ty', 'margot']
greet_user2.greet_users(usernames)

print("\n")

from greet_user2 import greet_users
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

print("\n")

from greet_user2 import greet_users as gu
usernames = ['hannah', 'ty', 'margot']
gu(usernames)

print("\n")

import greet_user2 as gu2
usernames = ['hannah', 'ty', 'margot']
gu2.greet_users(usernames)

print("\n")

from greet_user2 import *
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
