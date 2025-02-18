import math as m
from random import random

print("Lets play a game")
print('''If you guess a positive number from 1 to 100 right , you get a point''')


# condition checks for less than greater than and in between cases

#states
"""
1: <0.33
2: <0.67
3: <1"""

num=random()*10000
prev_state=0
err1=0
prev_err=0
while num!=num_in:
    prev_err=err1
    prev_state=state
    num_in = int(input("ENTER guess: "))
    err1=m.fabs(num_in-num)
    if err1/num <= 0.33:
        state =1
        if prev_state==1:
            if err1<prev_err:
                print("Your guess has exceeded your previous guess")
            else:
                print("Better guess but still err per <0.33")
        else:
            print("Error percentage <0.33")
    elif err1/num <= 0.66 and err1/num >0.33:
        state =2
        if prev_state==2:
            if err1<prev_err:
                print("Your guess has exceeded your previous guess")
            else:
                print("Better guess but still err per <0.66")
        else:
            print("Error percentage <=0.66")
    elif err1/num <= 1 and err1/num >0.66:
        state =3
        if prev_state==3:
            if err1<prev_err:
                print("Your guess has exceeded your previous guess")
            else:
                print("Better guess but still err per <1")
        else:
            print("Error percentage <=1")
    else:
        print("Something else")
        break
if num==num_in:
    print("Hurray! you got the right number")
else:
    print("better luck next time")


