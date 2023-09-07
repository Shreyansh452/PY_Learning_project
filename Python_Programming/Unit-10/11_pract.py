class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number **2} ")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number **3} ")
    
    def root(self):
        print(f"The value of {self.number} square root is {self.number **0.5} ")

    @staticmethod
    def greet():
        print("*****Welcome to the best calculator of the world!******")

a = Calculator(9)
a.greet()
a.square()
a.cube()
a.root()

   