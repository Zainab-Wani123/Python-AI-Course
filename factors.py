#function to create factors
def factors(n):
   print("The factors of", n, "are:")
   for i in range(1, n + 1):
        if n % i == 0:
            print(i)
#function call
# Input from the user
n = int(input("Enter a number to find its factors: "))
factors(n)
# This function calculates and prints the factors of a given number.
