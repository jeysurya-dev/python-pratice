class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('name:',self.name,'age:',self.age)
        print(f'Name: {self.name}, Age: {self.age}')

    def display(self):
        print(f'Name: {self.name}, Age: {self.age}')



p1 = Person('jey', 22)
p2 = Person('suriya', 15)
p3 = Person('amal',9)

p1.display()
p2.display()        
p3.display()





