from turtle import update


myDict = {
     "look" : "To see something",
     "apple" : "a kind of fruit",
     "Marks" : [1,3,4,5],
     'anotherdict' : {'shreyansh':'mishra ji'},
     1 : 2

}
# print(myDict["apple"])
# print(myDict['anotherdict']['shreyansh'])

# Dictionary Mathods
print(list(myDict.keys())) # Print key of  dictionary
print(myDict.values()) # Print values of  dictionary
print(myDict.items()) # Print keys and items of the dictionary
print(myDict)
updateDict = {
     "shreyansh" : "An intelligent boy",
     "Rohan"     : "Friend"
}
myDict.update(updateDict)  # Update the dictionary by adding keyvalues pair from update disk
print(myDict)
# Shows the value associated with  key "shreyansh"
print(myDict.get("shreyansh")) 
print(myDict["shreyansh"]) 
# Diffrence between .get and [] syntax in dictionaries
print(myDict.get("shreyansh2"))# It gives none when shreyansh2 not present in dictinary
# print(myDict(["shreyansh2"])   # It throws error when shreyansh2 not present in dictinary



