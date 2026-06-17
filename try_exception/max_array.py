'''from array import *
arr=array('i',[])
print(type(arr))
max=0
min=0

n=int(input("how many students in class"))
print("no of students=",n)

for i in range(n):
    marks=int(input("enter the marks"))
    arr.append(marks)

for i in arr:
    print(i)
  if max > i:
      max = i
print(max)'''
from array import *
from numpy import *

arr = array('i', [])

n = int(input("How many students in class: "))

for i in range(n):
    marks = int(input("Enter marks: "))
    arr.append(marks)

max = arr[0]
min = arr[0]

for i in arr:
    if i > max:
        max_marks = i

    if i < min:
        min_marks = i

print("Maximum marks =", max)
print("Minimum marks =", min)