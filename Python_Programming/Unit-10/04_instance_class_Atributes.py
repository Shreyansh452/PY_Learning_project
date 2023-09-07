from wsgiref.handlers import read_environ
from xml.etree.ElementPath import prepare_descendant


class Employee :
    company = "Google"
    salary = 200
    
shrey = Employee()
ravi = Employee()

# shrey.salary = 100
# ravi.salary = 200
shrey.salary = 400
print(shrey.salary)
print(ravi.salary)

# This line thorws error because address not present in instances/class
# print(ravi.address)




