string_to_list = ['Python', 'is', 'amazing' ]
message = ", ".join(string_to_list)
print("list to string:", message)
string_to_lists = message.split(", ")
print("string to list:", string_to_lists)




Shopping_List = ['Rice','Beans','Milk','Bread']
message = ", ".join(Shopping_List)
print("Shopping_List:", message)

string = message.split(", ")
print("Back to List:", string)


guest_list = ['faith', 'mary', 'helen', 'peter']

print(guest_list)

for guest in guest_list:
    print(f"Hi {guest.title()}, I'm inviting you to dinner with me.")