class bank:
  def __init__(emp,number,name):
      emp.account_number=number
      emp.full_name=name
  def deposit(emp):
     print("the account number is",emp.account_number,emp.full_name)

class invstor(bank):
    def __init__(self,number,name):
     super().__init__(number,name)
    def money(self):
        print("the account number is ",self.account_number,".my name is ",self.full_name)

x=invstor(51516551,"parva")
x.money()