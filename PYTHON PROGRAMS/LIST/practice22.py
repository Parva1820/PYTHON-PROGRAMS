#Find Maximum and Minimum in a List (without using max/min)
numbers=[1,2,3,4,50,6,7,8,9]
num=numbers[0]
for i in numbers:
    if i>num:
        num=i

print(num)
