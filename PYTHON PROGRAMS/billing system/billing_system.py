print("                                                                              AMUL DAIRY")
n = int(input("enter the numbers of item you are going to purchase:"))
i=1
total_cost=0
GST=0
while i<=n:
  for j in purchased_product:
    purchased_product=input("Enter purchased product: ")
    cost=int(input("Enter cost: "))
    total_cost += cost
    n -= 1
    print(purchased_product)
print("The total cost of your purchase is:",total_cost)
GST=total_cost*5/100
print("The GST of your purchase is:",GST)
GRAND_TOTAL=total_cost+GST
print("THE TOTAL AMOUNT IS: ",GRAND_TOTAL)
print("                                                                               INVOICE")
print("                                                                              AMUL DAIRY")
print("TOTAL NUMBER OF ITEMS PURCHASED",n)
print(purchased_product)


