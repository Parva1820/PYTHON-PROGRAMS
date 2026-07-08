#Merge Two Lists and Sort Them
num1=[1,3,2,4,8]
num2=[97,6,56,7,5]
def sorting():
  num1.extend(num2)
  print(num1)
  num1.sort()
  print(num1)

sorting()