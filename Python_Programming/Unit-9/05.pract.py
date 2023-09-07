f = open('poem.txt','r')
t = f.read()
if 'twinkle' in t:
    print("twinkle present in the file")
else:
    print("twinkle not present in the file")
f.close()