a = int(input(" kitna toffe chiye"))
total = 5
for i in range (1,a+1):
    if i<=total:
        print("toffe le lo apna ",i)
    else:
        print(" out of stock ")
        break
else:
    print("thank you visit again")
