string = "Bruce Wayne"
print(id(string))
string1 = string[:4] + "i" + string[5:]
print(string1)
print(id(string))

for char in string:
    print(f"unicode of '{char}': {ord(char)}")