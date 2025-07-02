'''. Ask the user to input three numbers. 
Print the largest of the three.'''
# variable to store the first number
num1 = int(input("Enter the first number: "))     
# variable to store the second number
num2 = int(input("Enter the second number: "))
# variable to store the third number
num3 = int(input("Enter the third number: "))
# check if the first number is greater than or equal to the second and third
if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
# check if the second number is greater than or equal to the first and third
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
# check if the third number is greater than or equal to the first and second
elif num3 >= num1 and num3 >= num2:
    print("The largest number is:", num3)
# if all numbers are equal
else:
    print("All numbers are equal.")
# End of code