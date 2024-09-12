class J:
    def __init__(self,name):
        self.name=name

    def display(self):
        print(self.name)
        print('parent')

class S(J):
    def __init__(self,name):
       super().__init__(name)
       super().display()
       self.name=name
       self.display()
       
    def display(self):
        print(self.name)
        print('child')
   

obj1=S("hello world")
obj1.display()
