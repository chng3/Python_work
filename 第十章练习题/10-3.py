# 10-3 访客

username = input("Please enter your username: ")

with open('guest.txt', 'w') as f:
	f.write(username)


# 10-4 访客名单

message = "Please enter your name: "
message += "\n(Enter 'q' at any time to quit)"

continues = True
while continues:
	name = input(message)
	if name == 'q':
		continues = False
	else:
		msg = "Hello, " + name.title() + "!"
		print(msg)
		with open('guest_book.txt', 'a') as f:
			f.write(msg + "\n")
	
	
# 10-5 关于编程的调查

filename = 'programming_poll.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(response + "\n")
