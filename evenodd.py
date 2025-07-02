# 1. Ask the user to enter a number. Check whether the number is even or odd and print the result.
# variable to store the number
num=int(input("Enter a number: "))
# check if the number is even or odd
if num % 2 == 0:
    print("The number is even.")
elif num % 2 != 0:
    print("The number is odd.")
