class phone():
    ramtype="256gb"
    def __init__(self,brand,price,chargetype):
        self.brand=brand
        self.price=price
        self.chargetype=chargetype
    def  display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("chargetype:",self.chargetype)
        print("Ramtype",self.ramtype)

googlepixel=phone("Googlepixel","10000","C-type")
sony=phone("Sony","5000","B-type")
googlepixel.display()
sony.display()
