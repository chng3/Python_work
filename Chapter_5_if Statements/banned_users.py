#检查特定值是否不包含在列表中

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:    #如果user的值未包含在列表banned_users中
    print(user.title() + ",you can post a response if you wish.")

