# While Loop

x = 0
# use while rather than "if" branching
while x < 5:
    # this will print after every "Loops"
    print("Not there yet, x=" + str(x) )
    # this will increment value of x
    x = x + 1
# if while is "False" this line will print
print("x=" + str(x))

 ## More while loop
 
def attempts(n):
    #   initializes the value x = 1
    x = 1
    while x <= n:
         print("Attempt " + str(x))
        #  the next line is just equal to "x = x + 1"
        #   this is also increment the value and loop back to the print statement
         x += 1
    print("Done")

#   this will call the func "attempts()"
attempts(5)

## Username sample
# this code will not run just a sample
username = get_username()

while not valid_username(username):
    print("Invalid Character")
    username = get_username()
    
