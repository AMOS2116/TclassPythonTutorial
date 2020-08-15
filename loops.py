# A for loop is used for iterating over a sequence ( list, tuple,dictionary, set, string)

students = ['Fortune', 'Abdul', 'Odinaka', 'Amos', 'Ibrahim', 'Zainab']


# Simple for loop

for student in students:
    print(f'I am: {student}')

# Break

for student in students:
    if student == 'Odinaka':
        break
    print(f'the student is: {student}')

# Continue

for student in students:
    if student == 'Odinaka':
        continue
    print(f'the people included: {student}')

# range

for person in range(len(students)):
    print(f'Number: {person}')

# custom range

for n in range(0, 12):
    print(f'Number: {n}')


# While loops execute a set of statements as long as a condition is true
 
count = 0
while count < 10:
    print(f'Count: {count}')
    count += 1