class Animal:
    animaType = "Mammal"

class Pet(Animal):
    color = "White"
  
class Dog(Pet):
    @staticmethod
    def bark():
        print(f"bow bow")
   
d = Dog()
d.bark()