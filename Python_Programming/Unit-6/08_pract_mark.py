from re import A


marks = int(input("Enter your marks: "))
if(marks>=90):
    grade = "Ex"                                              # print("Your grade is Ex")
elif(marks>=80):
    grade = "A"                         # print("Your grade is A")
elif(marks>=70):
    grade = "B"                                        # print("Your grade is B")
elif(marks>=60):
    grade = "C"                                             # print("Your grade is C")
elif(marks>=50):
    grade = "D"                                    # print("Your grade is D")
else:
    grade = "F"                                  # print("Your grade is f")
    
print("Your grade is " +grade)
