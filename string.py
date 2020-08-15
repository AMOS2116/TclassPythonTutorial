# Strings are iterables or collection of letters and numbers enclosed in a single or double quaot

name = "Onoo"

# +2347067162698 whatsapp


#prettier
#bracket pair coloriser
#live server

#"terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe"

my_name = 'Augustine Emeka Ekene'
print(my_name)

print(my_name.upper())
print(my_name.lower())
print(my_name.capitalize())

# Concatenation

print(my_name + ' ' + name)

# String Formatting

print(f' Hello, my name is {my_name}')

# Swap case
print(my_name.swapcase())

# Get length
print(len(my_name))

# Replace
print(my_name.replace('Ekene', 'Onoo'))

# Count
sub = 'e'
print(my_name.count(sub))

# Starts with
print(my_name.startswith('Augustine'))

# Ends with
print(my_name.endswith('e'))

# Split into List
print(my_name.split())

# Find position
print(name.find('n'))

# Is all alphanumeric
print(name.isalnum())

# Is all alphabetic
print(name.isalpha())

# Is all numeric
print(name.isnumeric())