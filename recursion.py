# RECURSION -> In programming, recursion is a way of doing a repetitive task by having a function call itself.

# Recursion example for Factorial

def factorial1(n):
    if n < 2:  # Base Case
        return 1
    return n * factorial1(n-1)  # Recursive case

# To see how this works with print


def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result


# call the func
factorial(5)

# Sample exercise

# The function sum_positive_numbers should return the sum of all positive numbers between the number n received and 1. 
# For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15. 
# Fill in the gaps to make this work:

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15