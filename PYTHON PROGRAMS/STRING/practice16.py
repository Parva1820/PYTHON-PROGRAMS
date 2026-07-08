#Reverse a String Without Using Built-in Function
y=str(input("enter any word: "))
for i in range(len(y)-1,-1,-1):
   print(y[i])