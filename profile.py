print("=" * 5, "MY PROFILE", "=" * 5)
users_name = input("Enter your name: ")
print(f"Short name: {users_name[:3]}")
users_age = int(input("Enter your age: "))
if users_age >= 18:

    print(f"{users_name}: You are an adult")
else:
    print(f"{users_name}: You are a minor")

hobbies = ["Reading", "Coding","Football"]
print("My hobbies:")
for number, hobby in enumerate(hobbies, start=1):
    print(f"{number}. {hobby}")

favorite_colors = ("red", "black")
print("favorite_color:" ,favorite_colors)
users_detail = {"name":users_name,"age":users_age,"hobby":hobbies,"favorite_color":favorite_colors}
print(users_detail)
print("=" * 25)
print(f"{users_name} {users_age}")
print( "=" * 25)