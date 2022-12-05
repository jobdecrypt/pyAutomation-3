# Fill in the blanks to make the factorial function return the factorial of n.
# Then, print the first 10 factorials (from 0 to 9) with the corresponding number.
# Remember that the factorial of a number is defined as the product of an integer and all integers before it.
# For example, the factorial of five (5!) is equal to 1*2*3*4*5=120.
# Also recall that the factorial of zero (0!) is equal to 1.

def factorial(n):
    result = 1
    for x in range(1, n):
        result = result * x
    return result


for n in range(0, 10):
    print(n, factorial(n+1))


##################

# Another way to program a USER Input and check FACTORIAL

number = input("Input Value to check factorial: ")
product = 1
for i in range(int(number)):
    product = product * (i+1)
print(product)
