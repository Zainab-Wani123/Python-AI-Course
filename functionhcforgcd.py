#function to create hcf ,gcd, lcm
def hcf(a, b):
    while b:
        a, b = b, a % b
    return a
def gcd(a, b):
    return hcf(a, b)
def lcm(a, b):
    return a * b // gcd(a, b)
#function call
# Input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
hcf_result = hcf(num1, num2)
gcd_result = gcd(num1, num2)
lcm_result = lcm(num1, num2)
print("HCF:", hcf_result)
print("GCD:", gcd_result)
print("LCM:", lcm_result)