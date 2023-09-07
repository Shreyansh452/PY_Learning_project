myDict = {
    "khana" : "food",
    "rupya": "Money",
    "sabji" : "vegitable"
}
print(myDict.keys())
a = input("Enter the hindi words for meaning:\n")
print("The meaning of your word is:",myDict[a] )
 
#  This will not show error if the searched element is not pressent
print("The meaning of your word is:",myDict.get(a) )
