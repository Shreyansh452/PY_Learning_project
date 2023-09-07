from operator import index


list1 = [3, 34, 23, "shreyansh", False, 3.24]

# index = 0 
# for item in list1:
#     print(item, index)
#     index += 1 

for index, item in enumerate(list1):
    print(item,index)