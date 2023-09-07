class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary of the employee working in {self.company} is {self.salary}")
     

shrey = Employee()
shrey.salary = 10000
shrey.getSalary()  #Employee.getSalary(shrey)