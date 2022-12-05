# def is_power_of_two(n):
#     # Check if the number can be divided by two without a remainder
#     while n != 0 and n % 2 == 0:
#         n = n / 2
#         # print(n)
#     # If after dividing by two the number is 1, it's a power of two
    
#     if n == 1: # or n / 2 == 2
#         return True

#     return False


# print(is_power_of_two(0))
# print(is_power_of_two(1))
# print(is_power_of_two(8))
# print(is_power_of_two(9))


def sum_divisors(n):    
    divisors = 1
    sum = 0

    while divisors < n:
        if n % divisors == 0:
            sum += divisors

        # print("the sum is " + str(sum))   
        # ELSE
        divisors += 1
    # Return the sum of all divisors of n, not including n
    return sum

print(sum_divisors(0))
print(sum_divisors(3))
print(sum_divisors(36))
print(sum_divisors(102))