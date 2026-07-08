class grandparents:
    def __init__(dsa,age,friends):
        dsa.age=age
        dsa.friends=friends

    def name(dsa):
        return dsa.age,dsa.friends

class parents(grandparents):
    def __init__(self,age,friends):
        self.age=age
        self.friends=friends
    def name(self):
        return self.age,self.friends

class child(parents):
    def __init__(dbms,age,friends):
        dbms.age=age
        dbms.friends=friends
    def name(dbms):
        return dbms.age,dbms.friends

g=grandparents(90,"MUKESH")
p=parents(50,"RAMESH")
c=child(22,"SURESH")
for i in (g,p,c):
    print(i.name())