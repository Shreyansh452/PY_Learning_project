# Creating empty set
b = set()
print(type(b))
#  Adding values to an empaty set
b.add(1)
b.add(1)
b.add(3)
b.add(3) # Adding value repeatadely does not changes a set
b.add((1,2,3,4))
print(b)
 
# b.add({4:5}) #can't add list dictonary to set
print(b)
print(len(b)) #Print the lenth of the set

#Removable of item
b.remove(3) #Remove 3 from the set
#b.remove(7)  # throw an error (7 is not present in set)
print(b)

print(b.pop())
print(b)