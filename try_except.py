try:
    n = int(input("Enter the N ="))
    d = int(input("enter the D ="))
    div = n/d
    print(n,"/",d,"=",div)
except ZeroDivisionError:
    print("You have enterted the value of D is zero")
except ValueError:
    print("You have enter a character")
except Exception:
    print("Something went wrong")
finally:
    print("thank you program closed")