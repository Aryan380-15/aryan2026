def multi(a,b):
    s=a+b
    sub=a-b
    div = a/b
    mul= a*b
    return s,sub,div,mul
q = multi(10,20)
print(q)
print(type(multi))
def inputting():
    a= int(input(" Enter a number ="))
    b= int(input(" Enter another number"))
    c = a+b
    print(" Sum of both number = ",c)
inputting()