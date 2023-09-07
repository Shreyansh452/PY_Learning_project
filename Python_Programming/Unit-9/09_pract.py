words = ["donkey","monkey","gadha","motu"]

with open("this.txt") as f:
    content = f.read()
    
for word in words:
    content = content.replace(word, "$%^@$^#")

with open("this.txt","w") as f:
    f.write(content)