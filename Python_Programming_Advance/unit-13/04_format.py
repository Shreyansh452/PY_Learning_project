name = 'Shreyansh'
course = 'Engineering'
branch = "AIML"
# a = f"This is {name}"
# a = f"This is {}".format{name}
# a = "My name  is {} and I'm doing {}".format(name, course)  # It takes the string in right order
a = "My name  is {0} and I'm doing {2} from the branch {1}".format(name, course, branch)  # It takes the string according to index number
print(a)