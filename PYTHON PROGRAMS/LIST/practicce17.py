#Find Second Largest Element in a List
list=[4,45,34,52,35,3,87]
l=list[0]
l_2=list[0]
for i in list:
    if i>l:
      l_2=l
      l=i
    elif i!=l and i>l_2:
        l_2=i

print(l)
print(l_2)
