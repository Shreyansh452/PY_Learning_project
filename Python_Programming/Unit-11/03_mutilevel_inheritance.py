class Person:
    country = "India"

    def __init__(self):
        print("Initializing the person.")
    
    def takeBreath(self):
        print("I am breathing...")



class Employee(Person):
    company = "TATA"

   

    def getSalary(self):
        print(f"The salary is {self.salary}")
   
    def takeBreath(self):
        super().takeBreath()
        print(f"I am employee so i'm luckily breathing.")


class Programmer(Employee):
    company = "Apple"

    def __init__(self):
        super().__init__()
        print("Initializing programmer...\n")

         
    def getSalary(self):
        print(f"NO salary for programmer")

    def takeBreath(self):
        super().takeBreath()
        print(f"I am programmer so i'm breating_+_+.")
     

# p = Person()
# p.takeBreath()


e = Employee()
# e.takeBreath()


# pr = Programmer() 
# pr.takeBreath()




