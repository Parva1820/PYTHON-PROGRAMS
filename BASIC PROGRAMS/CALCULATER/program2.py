#TO MAKE A SIMPLE CALCULATOR
x=int(input("Enter a number: "))
y=int(input("Enter another number: "))
def add(x,y):
    ans=x+y
    print(ans)
def sub(x,y):
    ans=x-y
    print(ans)
def mul(x,y):
    ans=x*y
    print(ans)
def div(x,y):
    ans=x/y
    print(ans)
print("PLEASE ENTRE THE OPERATION YOU Wnt to perform")
operation=input()
match operation:
    case "add":
        add(x,y)
    case "sub":
        sub(x, y)
    case "mul":
        mul(x, y)
    case "div":
        div(x, y)