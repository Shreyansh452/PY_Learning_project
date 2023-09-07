text = input("Enter the text: ")
# spam = False

if("make a lot of money" in text) :
    spam = True
elif("Buy now" in text):
    spam = True
elif("watch this" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is ham (not spam)")
