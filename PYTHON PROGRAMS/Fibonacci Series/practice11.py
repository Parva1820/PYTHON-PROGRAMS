#Fibonacci Series Print first n Fibonacci numbers.
x=0
y=1
next=0
while next < 10:
    next=x+y
    x=y
    y=next
    print(next)