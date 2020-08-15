# A Set is collection which is unordered and unindexed. No duplicate members

# Create a set
colours_set = {'red', 'yellow', 'green', 'white'}

print(colours_set)

# Check if in set

print('black' in colours_set)

# Add to set
colours_set.add('pink') 
print(colours_set)

# remove to set
colours_set.remove('pink') 
print(colours_set)

# Add duplicate to set
colours_set.add('yellow') 
print(colours_set)

# Clear Set
colours_set.clear()
print(colours_set)


# Delete set
del colours_set
print(colours_set)
