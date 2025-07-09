#function to find ascii value
def ascii_value(character):
    return ord(character)
# function call
# Input from the user
char = input("Enter a character: ")
result = ascii_value(char)
print("The ASCII value of ",char, "is", result)