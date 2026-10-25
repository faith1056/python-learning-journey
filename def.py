total_rooms = 20
rooms_taken = 8


def check_in():
    print("Guest checked in.")


def check_out():
    print("Guest checked out.")


def available_rooms():
    available = total_rooms - rooms_taken
    print("Available rooms:", available)


def taken_rooms():
    print("Rooms taken:", rooms_taken)



check_in()
check_out()
available_rooms()
taken_rooms()



def greet():
    print("Welcome!")
    print("How are you?")
    print("Have a nice day!")


def greet(name):
    print("Hello", name)

greet("Faith")
greet("John")


def multiply(a, b):
    return a * b

banana = multiply(4, 5)

print(banana)


def count_down(number):
    if number <= 0:
        return

    print(number)
    count_down(number - 1)

count_down(5)


def count(number):
    if number <= 0:
        return

    print(number)
    count(number - 1)

count(3)