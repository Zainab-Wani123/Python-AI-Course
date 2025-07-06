#input from user
num= int(input("Enter a number: "))
#sum of natural
#check if the number is positive
if num < 0:
    print("Please enter a positive number.")
else:
    sum = 0
    #calculate the sum of natural numbers
    for i in range(1, num + 1):
        sum += i
    print("The sum of natural numbers up to", num, "is:", sum)  
# End of code