#Find Common Elements Between Two Lists
list1=[1,2,3,4,5,6,7]
list2=[1,2,3,4,67,7,8]
list3=[]

def common():
   for i in list1:
      for z in list2:
        if i==z:
            list3.append(i)

   print(list3)

common()