#TO FIND WETHER THE GIVEN NUMBER IS PERFECT NUMBER OR NOT.
sum=0
x=int(input())
for y in range(1,6):
 if x%y==0:
  sum=sum+y
print(sum)

if sum==x:
 print("Yes," ,{x},  "is perfect number")
else:
 print("No," , {x} , "is not a perfect number")