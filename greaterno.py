'''5. Write a program that asks for two numbers and prints whether:
- The first is equal to the second
- The first is greater
- The second is greater'''
# variable to store the first number
num1 = float(input("Enter the first number: "))
# variable to store the second number
num2 = float(input("Enter the second number: "))
# check if the first number is equal to the second
if num1 == num2:
    print("The first number is equal to the second.")
# check if the first number is greater than the second
elif num1 > num2:
    print("The first number is greater than the second.")
# check if the second number is greater than the first
elif num2 > num1:
    print("The second number is greater than the first.")
# End of code
