from math import *
try:
    print("enter 1 for result")
    print("enter 2 for big number")
    print("enter 3 for quadratic eq")
    print("enter 4 foe find leap year")
    aa = int(input("enter a number  1 to 4  accourding to above"))
    match aa :
        case 1:
            math = int(input(" enter math number :"))
            science = int(input(" enter science number :"))
            english = int(input(" enter english number :"))
            hindi = int(input(" enter hindi number :"))
            sst = int(input(" enter sst number :"))
            total = math + science + english + hindi + sst
            print("Your total number is =",total)
            per = (total/500)*100
            print("Your percentage is =",per)
            if per < 33:
                print("Your fail ")
            elif 33 <= per < 45:
                print("Your pass with 3div")
            elif 45 <= per < 60:
                print("Your pass with 2div ")
            else:
                print("Your pass with 1div ")
        case 2:
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

        case 3:

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

        case 4:
            a = int(input(" Enter year"))
            if a % 4 ==0:
                if a % 100 ==0 and a % 400 == 0:
                    print(a,"is leap year")
                else:
                    print(a,"is not leap year")
            else:
                print(a,"is leap year")
        case _:
            print(" jitna bola jaye utna karo")

except ZeroDivisionError:
    print("You have enterted the value of D is zero")
except ValueError:
    print("You have enter a character")
except Exception:
    print("Something went wrong")
finally:
    print("thank you program closed")