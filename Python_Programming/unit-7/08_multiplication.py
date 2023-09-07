num = int(input("Enter the number "))
i = 1
for i in range(1, 11):
    print(str(num) + "X" + str(i) + "=" + str(i*num))
#     print(f"{num}X{i} ={num*i}") # We can use this f string to for table
# i = 1
# while i<=10:
#    print(str(num) + "X" + str(i) + "=" + str(i*num))
#    i = i+1