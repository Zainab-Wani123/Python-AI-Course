#input from user
num=int(input("number of terms: "))
#first two terms
n1, n2 = 0, 1
#check if the number of terms is valid
if num <= 0:
    print("Please enter a positive integer")
elif num == 1:
    print("Fibonacci sequence upto", num, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    print(n1,",", n2 , end=", ")
    for i in range(2, num):
        nth = n1 + n2
        print(nth, end=", ")
        # update values
        n1 = n2
        n2 = nth
    print(n1 + n2)
# End of code