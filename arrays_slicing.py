#slicing string
word = "PYTHON"

print(word[1:5])
#reverse a string
print(word[::-1])
#slicing tuples

#slicing tuples
numbers = (10,20,30,40,50)

print(numbers[1:4])

#slicing arrays
from array import array

numbers = array('i',[10,20,30,40,50])

print(numbers[1:4])
#slicing range 
numbers = range(1,11)

print(numbers[2:7])

#list slicing

numbers = [10,20,30,40]

numbers[1:3] = [200,300]

print(numbers)

#delete using slicing
numbers = [1,2,3,4,5]

numbers[1:4] = []

print(numbers)

#insert using slice 

numbers = [1,2,5]

numbers[2:2] = [3,4]

print(numbers)

#slices
names = ["John", "Mary", "Faith", "Peter"]

print(names[1:3])

numbers = [5,10,15,20,25]

print(numbers[:-2])

word = "PROGRAM"

print(word[::-1])


letters = ["A","B","C","D","E"]

print(letters[::2])



numbers = [1,2,3,4,5]

numbers[1:4] = [20,30]

print(numbers)