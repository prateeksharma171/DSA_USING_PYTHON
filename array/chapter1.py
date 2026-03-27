from array import *

val= array("i",[])

n=int(input("Enter the number of elements: "))
for i in range(n):
    x=int(input("Enter the element: "))
    val.append(x)

for i in val:
    print(i, end=" ")