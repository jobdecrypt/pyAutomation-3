# Quiz 1

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
    
# Quiz 2

# Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.

# for x in range(1,11):
#     print(x**3)

# Quiz 3

# Write a script that prints the multiples of 7 between 0 and 100. 
# Print one multiple per line and avoid printing any numbers that aren't multiples of 7. 
# Remember that 0 is also a multiple of 7.

# for y in range(0,100):
#     if y % 7 == 0:
#         print(y)

# Quiz 4

# The retry function tries to execute an operation that might fail, it retries the operation for a number of attempts.
# Currently the code will keep executing the function even if it succeeds. 
# Fill in the blank so the code stops trying after the operation succeeded.

## The next Code will run only on the Sandbox of the QUIZ


# def retry(operation, attempts):
#     for n in range(attempts):
#         if operation():
#             print("Attempt " + str(n) + " succeed")
#             break
#         else:
#             print("Attempt "+ str(n) + " failed")

# retry(create_user, 3)
# retry(stop_service, 5)



##################

# Another way to program a USER Input and check FACTORIAL

# number = input("Input Value to check factorial: ")
# product = 1
# for i in range(int(number)):
#     product = product * (i+1)
# print(product)