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

   