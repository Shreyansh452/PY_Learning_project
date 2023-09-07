from tokenize import Single


# Single Inheritance
class Employee:
    company = "Google"
    
    def showDetail(self):
        print("This is an employee.")

class Programmer(Employee):
    language = "Python"
    company = "Youtube"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetail(self):
        print("This is an programmer")

e = Employee()
e.showDetail()
p = Programmer()
p.showDetail()
print(p.company)