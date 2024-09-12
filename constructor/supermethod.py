class Jey:

    def name(self):
        print('nirmal')
    


class Nimo(Jey):

    def name(self):
        print('nimo')

    def sub(self):
        super().name()
        self.name()

obj=Nimo()
obj.sub()
