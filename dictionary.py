# A Dictionary is a collection which is unordered, changeable and indexed. Noduplicate members.

# Create Dictionary

person_detail = {
    'first_name': 'Augustine',
    'last_name': 'Emeka',
    'age': 30
}

# Use of a constructor

person_details2 = dict(first_name='Husseini', last_name='Suleiman')

print(person_detail)

# Get a Value
print(person_detail['first_name'])

# Add key/value
person_detail['phone_number'] = '+2347067162698'
print(person_detail)

# Get dictionary keys
print(person_detail.keys())

# Get dictionary items
print(person_detail.items())

# Copy dictionary
person_information = person_detail.copy()
print(person_information)

# Remove item
del (person_detail['last_name'])
person_detail.pop('phone_number')
print(person_detail)

# Clear
#person_detail.clear()
print(person_detail)

# Get Length
print(len(person_detail))

# Make a List of dictionaries
persons = [
    {'name': 'Augustine', 'age': 35, 'phone_number': '+2347067162698'},
    {'name': 'Fortune', 'age': 21, 'phone_number': '+2347083915552'},
    {'name': 'Ola', 'age': 30, 'phone_number': '+2348156243419'}
]

print(persons[1]["name"])