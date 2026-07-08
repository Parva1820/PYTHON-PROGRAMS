#using multidimentional array display table of 5-7 student data base.
class student:
    def __init__(self,name,age,roll_number):
        self.name=name
        self.age=age
        self.roll_number=roll_number

    def  __str__(self):
        return f'{self.name} {self.age} {self.roll_number}'

std1=student("PARVA R. SHARMA",19,376)
std2=student("KRISHNA PANDIT",16,375)
print(std1)
print(std2)