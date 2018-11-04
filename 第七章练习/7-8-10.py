# 7-8 熟食店

sandwich_orders = ['pastrami', 'tuna', 'derr', 'pastrami', 'derr', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
       finished_sandwich = sandwich_orders.pop()
       print("I made your " + finished_sandwich + " sandwich.")
       finished_sandwiches.append(finished_sandwich)

print(finished_sandwiches)
print("\n")

# 7-9 五香烟熏牛肉
sandwich_orders = ['pastrami', 'tuna', 'derr', 'pastrami', 'derr', 'pastrami']
finished_sandwiches = []
print("The pastrami solded!")

while 'pastrami' in sandwich_orders:
       sandwich_orders.remove('pastrami')

while sandwich_orders:
       finished_sandwich = sandwich_orders.pop()
       finished_sandwiches.append(finished_sandwich)
print(finished_sandwiches)

# 7-10 梦想的度假胜地
places = {}

research_active = True

while research_active:
       name = input("\nWhat is your name? ")
       place = input("If you could visit one place in the world, where would you go? ")
       places[name] = place
       repeat = input("Would you like to let anthoner person respond?(yes/ no) ")
       if repeat == 'no':
              research_active = False

              
print("\n--- Research Results ---")
for name, place in places.items():
       print(name.title() + " like to visit " + place.title() + "!")
