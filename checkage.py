'''Write a program that asks for the user's age and prints: "Child" if age < 13, 
 "Teenager" if age is between 13 and 19, "Adult" if age is 20 or more'''
# variable to store the age
age=int(input("Enter your age: "))
# check the age and print the result
if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20:
    print("Adult")
