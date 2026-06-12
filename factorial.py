a = int(input(" ENTER NUMBER U WANT !"))
fact = 1
i = 1
while i <= a:
    fact = fact*i
    print(" ",i,"X",end='')
    i = i+1
print(" = ",fact)