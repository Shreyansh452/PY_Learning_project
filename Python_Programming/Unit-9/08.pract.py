with open("this.txt") as f:
    content = f.read()
    

content = content.replace("donkey", "$%^@$^#")

with open("this.txt","w") as f:
    f.write(content)