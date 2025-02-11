import math as m

from random import random

print("Lets play a game")
print('''If you guess a positive number from 1 to 100 right , you get a point''')


# condition checks for less than greater than and in between cases

num=random*10000
prev_state=0
while num!=num_in:
    num_in = int(input("ENTER : "))
    if num_in < 0.33*(num_in-num):
        state =1
        if prev_state==1:

