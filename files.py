# Python has functions for creating, reading, updating, and deleting files

# Open a file

ekeneFile = open('austine.txt', 'w')

# Get Information

print('Name: ', ekeneFile.name)
print('Is Closed: ', ekeneFile.closed)
print("Opening Mode: ", ekeneFile.mode)

# Write to File
ekeneFile.write('Ekene is my Igbo name')
ekeneFile.write(' I am from Anambra State')
ekeneFile.close()

# Append to file
ekeneFile = open('austine.txt', 'a')
ekeneFile.write(" I also live in Abuja Nigeria and I love Python")
ekeneFile.close()


# Read from file

ekeneFile = open('austine.txt', 'r+')
text = ekeneFile.read(100)
print(text)