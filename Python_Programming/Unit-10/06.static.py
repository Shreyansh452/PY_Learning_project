class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary of the employee working in {self.company} is {self.salary}\n {signature}")

    @staticmethod
    def greet():
        print("Good Morning,shrey")

    @staticmethod
    def time():
        print("Time is 9 am in the morning. ")

shrey = Employee()
shrey.salary = 10000
shrey.getSalary("Thanks!")  #Employee.getSalary(shrey)
shrey.greet()
shrey.time()