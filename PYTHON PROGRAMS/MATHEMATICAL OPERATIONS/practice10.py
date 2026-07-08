#Count Digits in a Number
x=12345
count=0
if x==0:
    count=1
else:
  while x!=0:
    x//=10
    count+=1

print(count)