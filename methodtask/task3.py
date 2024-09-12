class bank:
    def interest(self):
        print("interest:9")
        

class icic(bank):
    def interest(self):
        super().interest()
        print("interest:5")
    

class canara(bank):
    def interest(self):
        print("interest:6")

class kvb(bank):
    def interest(self):
        print("interest:7")
#obj=bank()
obj1=icic()
obj2=canara()
obj3=kvb()
#obj.interest()
for j in (obj1,obj2,obj3):
    j.interest()
