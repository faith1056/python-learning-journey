favorite_fruits = ['mango','banana','orange','apple','berries']
if 'mango' in favorite_fruits:
    print("i love mango")
if 'banana' in favorite_fruits:
    print("i love banana")
if 'orange' in favorite_fruits:
    print("i love orange")
if 'apple' in favorite_fruits:
    print("i love apple")
if 'berries' in favorite_fruits:
    print("i love berries")

if 'banana' in favorite_fruits:
    print("i really like banana")
if 'orange' in favorite_fruits:
    print("i really like orange")
if 'apple' in favorite_fruits:
    print("i really like apple")
if 'berries' in favorite_fruits:
    print("i really like berries")

requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    print("Adding" + requested_topping + ".")

print("\nFinished making your pizza!")

if requested_topping == 'green peppers':
    print("sorry, we are out of green peppers right now.")

user_names = ['admin', 'peace','faith','mary','dorcas']
for user_name in user_names:
    print(f"{"welcome back online"} , {user_name}")


for user_name in user_names:

    if user_name == 'admin':
        print("Hello admin , will you like to see a status report?")
else:

    print(f"Hello {user_name} thank you for logging in again")
#else:
    #print("we need to find users")