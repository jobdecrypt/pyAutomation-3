my_var = 1

while my_var <= 10:
    print("Hello " + str(my_var))
    my_var += 1

####################

x = 1
sum = 0
while x < 10:
    sum += x
    # print(sum)
    x += 1

# print(x)

product = 1
while x < 10:
    product = product * x
    x += 1
# NOTE: The print will RUN but the result is wrong because the condition "x < 10" is wrong cause the current value of x is 10
print(sum, product)

def print_range(start, end):
    	# Loop through the numbers from start to end
	n = start
	print(n)
	while n < end:
		n +=1
		print(n)

print_range(1, 5) 

############################### 



