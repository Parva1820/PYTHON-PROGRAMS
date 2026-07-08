#Print All Prime Numbers in a Range
for i in range(2,10):
    for j in range(2,i+1):
      if i%j==0:
        print(i)
