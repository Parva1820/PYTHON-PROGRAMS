products={
    1:{"name":"CHOCOLATE   ","price":50},
    2:{"name":"BANANA      ","price":50},
    3:{"name":"CHIPS       ","price":10},
    4:{"name":"COLD DRINKS ","price":20},
    5:{"name":"MILK        ","price":25}
}

# Class for Billing System
class BillingSystem:


    def __init__(self):
        self.cart = {}

    def show_products(self):
        print("\n------ Available Products ------")
        print("ID   Name         Price")
        for pid, pdata in products.items():
            print(pid, " ", pdata["name"], "   Rs.", pdata["price"])
    def basket(self):
        print("\n------ Basket ------")
        while True:
           selected_product = int(input("Select a Product: "))
           if selected_product in products:
              print("\n valid Selection ")
              self.cart[selected_product] = products[selected_product]
           else:
              print("\n Invalid Selection ")
              break

        print(self.cart)
    def purchase(self):
        print("\n------ Purchase ------")
        print(self.cart)

    def total_cartprice(self):
        #TOTAL AMOUNT OF PRICE WHICH ARE ADDED INTO THE CART
        total = 0
        for item in self.cart:
            total = total + self.cart[item]["price"]

        print("Total cart Price is : ", total)

#GST ON THE TOTAL BILL
        total_gst = 0
        print("INCLUDING GST")
        GST=int(input("GST: "))
        total_gst = total * GST /100
        print("TOTAL GST INCLUDED",total_gst)

#DISCOUNT GIVEN ON THE TOTAL BILL
        discounted_bill=0
        print("DISCOUNT ON THE TOTAL BILL INCLUDING GST")
        DIS=int(input("DISCOUNT: "))
        discounted_bill= (total_gst - DIS)/100
        print("DISCOUNT GIVEN ON THE TOTAL BILL INCLUDING GST IS : ",discounted_bill)

        #ADD GST AND MINUS DISCOUNT FROM THE TOTAL BILL
        total_CART = 0
        total_CART=total-discounted_bill+total_gst
        print("TOTAL PURCHACE AMOUNT COUSTOMER NEEDS TO PAY IS : ",total_CART)









p1=BillingSystem()
p1.show_products()
p1.basket()
p1.purchase()
p1.total_cartprice()
#p1.total_billing_price()
import datetime
purchace_time=datetime.datetime.now()
print("---------------------------------------------------------------------INVOICE------------------------------------------------------------------------------------")
print("                                                                                                                                                  ",purchace_time)
p1.purchase()
p1.total_cartprice()
