class Employee:
    company = "Accenture"
    eCode = 231

class Freelancer:
    company = "Fever"
    level = 0

    def upgradeLevel(self):
     self.level = self.level + 1

class Programmer(Employee, Freelancer):
    name = "shreyansh"


p = Programmer()
p.upgradeLevel()
print(p.level)






