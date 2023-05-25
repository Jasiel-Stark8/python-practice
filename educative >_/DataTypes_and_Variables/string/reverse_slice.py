string = "Mr-Bruce-Wayne"
print(string[11:2:-2]) # Take 2 steps back. The opposite of what happens in the forward slicing

# Partial slicing
print(string[:8])  # All the characters before 'M'
print(string[8:])  # All the characters starting from 'M'
print(string[:])  # The whole string
print(string[::-1])  # The whole string in reverse (step is -1)

# Specifying the start and end indices is optional.

# If start is not provided, the substring will have all the characters until the end index.

# If end is not provided, the substring will begin from the start index and go all the way to the end.