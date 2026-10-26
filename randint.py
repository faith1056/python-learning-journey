from random import randint

count = 0
for i in range(10000):
    number = randint(1,100)
    if number%12==0:
        count=count+1
    

print('Number of multiples of 12:',count)

from random import randint
rand_num = randint(5,25)
for i in range(rand_num):
    print( 'Hello ')
