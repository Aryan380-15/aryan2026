'''
a = int(input("enter the number u want fibonacci turm"))
a1 = 0
a2 = 1
i = 1
while i<=a:
    print(a1,end='')
    a3 = a1 + a2
    a1 = a2
    a2 =a3
    i = i+1
'''
a = int(input("Enter the number of Fibonacci terms: "))

a1 = int(input(" enter 1 number: "))

a2 = int(input(" enter 2 number1: "))

i = 1

while i <= a:
    print(a1, end=' ')
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    i = i + 1