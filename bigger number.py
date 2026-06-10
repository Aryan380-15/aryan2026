'''
a = int(input(" enter A"))
b = int(input(" enter B"))
c = int(input(" enter C"))
if a > b:
    if a > c:
        print(a,"is bigger")
    else:
        print(c,"is bigger")
elif b > c:
    print(b,"is bigger")
else:
    print(c,"is bigger")
    '''

a = int(input(" enter A"))
b = int(input(" enter B"))
c = int(input(" enter C"))
if a > b:
    if a > c:
        print(a," a is bigger")
    else:
        print(c," c is bigger")
else:
    if b > c:
        print(b," b is bigger")
    else:
        print(c," c is bigger")