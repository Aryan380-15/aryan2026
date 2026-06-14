'''
a =int(input("enter a number u want to know is prime ="))
flag = 0
i = 2
while i < a:
    if a%i == 0:
        flag = flag + 1
        break
    else:
        flag = 0
    i = i+1
if flag == 0:
    print(a," is a prime number")
else:
    print(a," is a not prime number")

'''
a = int(input(" kiska prime janna hai number do ="))
i = 2
while i < a:
    if a%i == 0:
        print(a," is a not prime number")
        break
    i = i+1

else :
    print(a," is a prime number")