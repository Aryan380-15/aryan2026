a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if a == b == c:
    print("A, B and C are equal")

elif a > b and a > c:
    print(a, "is bigger")

elif b > a and b > c:
    print(b, "is bigger")

elif c > a and c > b:
    print(c, "is bigger")

elif a == b:
    print("A and B are equal")

elif b == c:
    print("B and C are equal")

else:
    print("A and C are equal")