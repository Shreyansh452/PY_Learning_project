from xml.etree.ElementInclude import include


letter = '''dear <Name>
Greetings I am very happy to say you that our selection procedure is over for coding hub and 
your are  selected!
I hope you will    grow and go  ahed in your    life.
regrads 
raunak
Date : <Date>
'''

name = input("Enter your name \n")
date = input("Enter Date\n")
letter = letter.replace("<Date>",date)
letter = letter.replace("<Name>",name)
letter = letter.capitalize()
letter = letter.replace("    "," ")

print(letter)