# File IO in Python


# Modes in files

# 1.read()  2.write()  3.append()  4.text()  5.create()  6.binary()

# Reading a file
f = open('hammad2.py', 'r') # read (r) mode is default
print(f)
text = f.read()
#print(text)
f.close()

# writing a file


f = open('hammad2.py', 'w')
f.write("Hello, world!")
f.close()


# THe "with" satement

with open("hammad.py", 'a') as f:
    f.write("Hey I am inside with")