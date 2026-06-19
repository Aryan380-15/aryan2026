# 1. positional argument passing
def person(name,age):
    print(name,age)
person("Ram",18)

# why it is position argument
def person0 (name,age):
    age= age+10
    print(name,age)
# person0(18,"ram") isme position alag
person0('rama',18)

# 2. keyword argument passing
def person1(name,age):
    age = age + 18
    print(name,age)
person1(name = "aryan", age = 18)
person1( age = 10 ,name = "diwan")

#3. variable length argument
def calci(a,*b):
    s=a             #  *b iske use se hum ek tuple bana skate hai
    for i in b:
        s = s+i
    return s

z =calci(10,20,30,40,50,60,70,80,90)
print("sum of all geven number is =",z)

# 4. keyword variable length argument
def bio(**data):
    print(data) # ** iske under hun Dictionary

bio(name='aryan',age=18,classs='CSE',collage='Maharana Partap polytechnic Gorakhpur')




