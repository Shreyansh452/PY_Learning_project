# marks = [88,78,89,99]
# percentage1 = (sum(marks)/400)*100                                                
# marks2 = [23,33,43,54]
# percentage2 = ((marks2[0]+marks2[1]+marks2[2]+marks2[3])/400)*100
# print(percentage1,percentage2)

# This is by the function.

def percent(marks):
       return((marks[0]+marks[1]+marks[2]+marks[3])/400)*100


marks1 = [88,78,89,99]
percentage1 = percent(marks1)

marks2 = [23,33,43,54]
percentage2 = percent(marks2)
print(percentage1,percentage2)