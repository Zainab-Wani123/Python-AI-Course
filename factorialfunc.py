#function for factorial
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
# Function call
# Input from the user
n = int(input("Enter a positive integer: "))
result = factorial(n)
print("The factorial of", n, "is", result)