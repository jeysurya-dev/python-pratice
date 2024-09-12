class grandpa():
    def phone(self):
        print("grandpa phone")

class dad(grandpa):
    def money(self):
        print("Dads money")

class son(dad):
    def laptop(self):
        print("Son laptop")

surya=son()
surya.phone()


