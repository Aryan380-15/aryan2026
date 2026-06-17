# Armstrong Number isme  single digit ka ^3 fir unka sum same hota

b = int(input(" kis range ta ka armstrong number chiye batao ="))
for n in range(1,b):
    orig=n
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit*digit*digit
        n=n//10
    if orig==sum:
        print(sum,"armstrong no")
    else:
        pass
