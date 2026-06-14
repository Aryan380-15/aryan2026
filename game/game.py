from random import *
n=randint(1,100)
for i in range (0,4):
    a = int(input("gass a number : "))
    if a == n:
        print("you win ")
        break
    else:
        print("try again")
else:
    print("you loss becouse the number is ",n)


