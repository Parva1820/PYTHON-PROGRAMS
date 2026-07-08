#Take three numbers as input and print the largest.
print("enter any three numbers")
x=int(input())
y=int(input())
z=int(input())

max=x
if y>max:
    max=y
if z>max:
    max=z
print(max)