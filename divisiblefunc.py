#function to declare the divison
def dev_num(num1, num2):
    if num2 == 0:
        return "Division by zero is not allowed."
    else:
        return num1 / num2
#function call
# Input from the user
n1 = float(input("Enter the first number (numerator): "))
n2 = float(input("Enter the second number (denominator): "))
result = dev_num(n1, n2)
print("The result of the division is:", result)