# Use open function to read content of file.

# f = open('sample.txt', 'r')
f = open('sample.txt')   # It outomatically takes r to read.
# data = f.read()
data = f.read(9)   # It takes only 9 initial words from file.
print(data)
f.close()