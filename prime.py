#input from user
num=int(input("Enter a number: "))
#check if the number is prime
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
        # End of code
