class grandparent:
    def __init__(self,color,hobby):
        self.skin_color=color
        self.daily_routine=hobby
    def show(self):
        print("Their skin color is ",self.skin_color,". And their hobbies are ",self.daily_routine)
class parents(grandparent):
    def __init__(dsa,color,hobby):
        super().__init__(color,hobby)
        dsa.age=age
    def routine(dsa):
        print
x=parents("brown","cricket")
x.show()