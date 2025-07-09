#function for add two numbers
def add_numbers(a, b):
    return a + b
# function for multiply two numbers
def multiply_numbers(a, b):
    return a * b
# function call 
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
# displaying the sum
sum_result = add_numbers(num1, num2)
print("The sum of the two numbers is:", sum_result)
# displaying the product
product_result = multiply_numbers(num1, num2)
print("The product of the two numbers is:", product_result)