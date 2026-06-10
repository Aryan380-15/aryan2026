'''
a = int(input(" Enter year"))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(a,"is leap year")
else:
    print(a,"is not leap year")
'''
a = int(input(" Enter year"))
if a % 4 ==0:
    if a % 100 ==0 and a % 400 == 0:
        print(a,"is leap year")
    else:
        print(a,"is not leap year")
else:
    print(a,"is leap year")
