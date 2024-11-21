# seek(), tell() and other functions


# seek() function
with open('myfile.txt', 'r') as f:
    print(type(f))
    # Move to the 10th byte in the file
    f.seek(10)

    # Read the next 5 bytes
    data = f.read(5)
    print(data)

# tell() function


with open('myfile.txt', 'r') as f:
    print(type(f))
    # Move to the 10th byte in the file
    f.seek(10)
    print(f.tell())
    # Read the next 5 bytes
    data = f.read(5)
    print(data)

# truncate() function

with open('sample.txt', 'w') as f:
    f.write('Hello World!')
    f.truncate(3)

with open('sample.txt', 'r') as f:
    print(f.read())