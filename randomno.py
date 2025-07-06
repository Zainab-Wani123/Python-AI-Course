#random number generator
num=int(input("Enter a number: "))
import random
# Generate a random number between 1 and the input number
random_number = random.randint(1, num)
# Print the random number
print("Random number between 1 and", num, "is:", random_number)
# End of code