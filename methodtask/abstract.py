from abc import ABC

class Car(ABC):
    def type(self):
        pass
    
class swift(Car):
    def type(self):
        print("desire")

class Bmw(Car):
    def type(self):
        print("fast")

class ford(Car):
    def type(self):
        print("slow")
        

obj1=swift()
obj1.type()
obj2=Bmw()
obj2.type()
obj3=ford()
obj3.type()


