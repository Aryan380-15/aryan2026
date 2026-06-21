def total():
    math= int(input("Enter the math number ="))
    science= int(input("Enter the science number ="))
    english= int(input(" Enter the english number ="))
    hindi= int(input("Enter the hindi number ="))
    sst= int(input(" Enter the sst number ="))
    sum = math+science+english+hindi+sst
    return sum
s=total()
print(" your total number is =",s,"/500")
