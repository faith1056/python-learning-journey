import sys

numbers_list = [10,20,30,40]
numbers_tuple = (10,10,30,40)


print("List memory:", sys.getsizeof(numbers_list))
print("Tuple_memory:", sys.getsizeof(numbers_tuple))

#tuple concatenation
coordinates = (10, 20, 30)

coordinates = coordinates + (40,)

print(coordinates)


#compiler optimize tuples
import dis

def get_directions():
    return ("north", "south", "east", "west")

dis.dis(get_directions)