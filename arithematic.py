'''Write a program that takes two numbers from the user and prints their: Sum, Difference, Product, Quotient (division), 
Remainder (modulus),Power (first number raised to the second)'''
# variable to store the first number
num1 = float(input("Enter the first number: "))
# variable to store the second number
num2 = float(input("Enter the second number: "))
# calculate the sum
sum_result = num1 + num2
# calculate the difference
diff_result = num1 - num2
# calculate the product
prod_result = num1 * num2
# calculate the quotient
if num2 != 0:
    quot_result = num1 / num2
else:
    quot_result = "undefined (division by zero)"
# calculate the remainder
if num2 != 0:
    rem_result = num1 % num2
else:
    rem_result = "undefined (division by zero)"
# calculate the power
pow_result = num1 ** num2
# print the results
print("sum:", sum_result)
print("difference:", diff_result)
print("product:", prod_result)
print("quotient:", quot_result)
print("remainder:", rem_result) 
print("power:", pow_result)
# End of code
