a = int(input("enter digit u want sum = "))
sum = 0
while a >0:
    digit = a%10
    sum = sum + digit
    a = a//10
print(sum)