#3-4
#嘉宾名单
guest = ["Kevin", "Melo", "Harden"]
print(guest[0] + "," + guest[1] + ',' + guest[2] + ',' + "we sincerely invite you to have dinner with us.\n")

#3-5
#修改嘉宾名单
print("Oh, because of something reasons, Melo will absent our dinner,and we should invite another one.\n")

guest[1] = 'Paul'
print(guest[0] + "," + guest[1] + ',' + guest[2] + ',' + "we sincerely invite you to have dinner with us.\n")

#3-6
#添加嘉宾
print("I found a big table right now, we could invite more and more people we want.\n")

guest.insert(0,"窦文涛")
guest.insert(2,"马未都")
guest.append("高晓松")
print(guest[0] + "," + guest[1] + ',' + guest[2] + ',' + guest[3] + "," + guest[4] + "," + guest[5] + "," + "we sincerely invite you to have dinner with us.\n")

#3-7
#缩减名单
print("Sorry, we can only invite two guess right now.\n")
popped_guest1 = guest.pop()
print("Sorry, " + popped_guest1 + " we have to exclude you.\n")
popped_guest2 = guest.pop()
print("Sorry, " + popped_guest2 + " we have to exclude you.\n")
popped_guest3 = guest.pop()
print("Sorry, " + popped_guest3 + " we have to exclude you.\n")
popped_guest4 = guest.pop()
print("Sorry, " + popped_guest4 + " we have to exclude you.\n")

print(guest[0] + ", " + guest[1] + ", " + "Luckily! you two guest can stll have dinner with me!\n")

#删除最后两位嘉宾
del guest[0]
del guest[0]    

print(guest)
