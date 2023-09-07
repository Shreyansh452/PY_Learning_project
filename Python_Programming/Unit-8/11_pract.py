def remove_and_split(string,word):
    newStr = string.replace(word,"")
    return newStr.strip()

this = "     shreyansh is a good boy     "
n = remove_and_split(this,"shreyansh")
print(n)
