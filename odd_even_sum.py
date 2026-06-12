a = int(input("Enter start: "))
b = int(input("Enter stop: "))

even = odd = 0

if a < b:
    i = a
    while i <= b:
        if i % 2 == 0:
            print("even =", i)
            even += i
        else:
            print("odd =", i)
            odd += i

        i += 1

else:
    i = a
    while i >= b:
        if i % 2 == 0:
            print("even =", i)
            even += i
        else:
            print("odd =", i)
            odd += i

        i -= 1

print("Sum of even =", even)
print("Sum of odd =", odd)