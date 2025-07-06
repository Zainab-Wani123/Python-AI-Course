#input from user
import math
#input coefficients of quadratic equation
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
#calculate the discriminant
discriminant = b**2 - 4*a*c
#check if the discriminant is positive, negative or zero
if discriminant > 0:
    #two real and distinct roots
    discriminant_sqrt=discriminant**0.5
    root1 = (-b + discriminant_sqrt) / (2 * a)
    root2 = (-b - discriminant_sqrt) / (2 * a)
    print("The roots are real and distinct:")
    print("Root 1:", root1) 
    print("Root 2:", root2)
elif discriminant == 0:
    #one real root
    root = -b / (2 * a)
    print("The root is real and repeated:")
    print("Root:", root)
else:
    #complex roots
    real_part = -b / (2 * a)
    discriminant_sqrt = -discriminant**0.5
    imaginary_part = discriminant_sqrt / (2 * a)
    root1 = complex(real_part, imaginary_part)
    root2 = complex(real_part, -imaginary_part)
    print("The roots are complex:")
    print("Root 1:", root1)
    print("Root 2:", root2)
# End of code