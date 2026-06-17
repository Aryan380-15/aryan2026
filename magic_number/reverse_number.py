b = int(input("Enter a number: "))

for a in range(1, b + 1):
    c = a
    riv = 0

    while a > 0:
        digit = a % 10
        riv = riv * 10 + digit
        a = a // 10

    if c == riv:
        print(c, "is a palindrome number")