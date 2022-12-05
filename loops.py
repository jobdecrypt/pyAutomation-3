# initializing first the variable

my_variable = 5

while my_variable < 10:
    print("Hello")
    my_variable += 1

# sample initializing variable before loop


def count_down(start_number):

    current = start_number

    while (current > 0):
        print(current)
        current -= 1

    print("Zero!")


count_down(3)


# Sample initialization and while loop for variable x.
x = 0
# to avoid "infinite loop"
if x != 0:
    # while loop
    while x % 2 == 0:
        x = x / 2

# another sample to eliminate "if" statement above
# using the conditional "and"
while x != 0 and x % 2 == 0:
    x = x / 2

# example to print range from "start" to "end"


def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    print(n)
    while n < end:
        n += 1
        print(n)


print_range(1, 5)

# Sample loop using "break"

# while True:
#     do_something_cool()
#     if user_requested_to_stop():
#         break
