# for loop is used when there's a sequence of elements that you want to iterate

# Samples

for x in range(5):
    print(x + 1)

# Sample 2

friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)

# Sample 3
# You can use this loop to "Copy files to machines", "Process the contents of files" and "Automatically install software"
values = [23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum/length))

# Sample 4
# initiatize product to 1
product = 1
# for n in range 1 to 10
for n in range(1, 10):
    product = product * n
print(product)

# Sample 5


def to_celsius(x):
    # conversion formula from Fahrenheit to Celsius
    return (x-32)*5/9


# for x in range from 0 to 101 and 10 is the 3rd parameter by 10 size
# range Function has 3 parameters, 1st is the start, 2nd is the limit, 3rd is the size gap or increased time steps
for x in range(0, 101, 10):
    print(x, to_celsius(x))

# Job's Sample
for y in range(0, 51, 2):
    print(y)
