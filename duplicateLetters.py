## initializing string
string = "ananya"
## initializing a list to append all the duplicate characters
duplicates = []
for char in string:
   ## checking whether the character have a duplicate or not
   ## str.count(char) returns the frequency of a char in the str
   if string.count(char) > 1:
        if char not in duplicates:
            duplicates.append(char)
print(duplicates)