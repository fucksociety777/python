class Animal: # this is parent class (Super class)
    def __init__(self, name):
        self.name = name
    def speak(self):
            print("speaking now....")

class Dog(Animal): 
    def speak(self):
        super().speak()
        print("Woof!!!")

d = Dog("Bruno") 
d.speak()      