from math import *
from math import *

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = b*b - 4*a*c

if d > 0:
    x1 = (-b + sqrt(d)) / (2*a)
    x2 = (-b - sqrt(d)) / (2*a)
    print("Real and Distinct Roots")
    print(x1, x2)

elif d == 0:
    x = -b / (2*a)
    print("Real and Equal Roots")
    print(x)

else:
    print("Imaginary Roots")