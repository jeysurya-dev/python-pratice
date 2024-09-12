# Python code to illustrate split() function
with open("jey.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)
