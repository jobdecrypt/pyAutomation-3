# Loops within a loop or Nested For Loop

# Sample 1
# Dominoes Sample
for left in range(7):
    for right in range(left, 7):
        # print Parameter "end" that create's a new line or " "
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()


# Sample 2

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    # print(home_team)
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

# Sample 3
# int is NOT iterable

# this next line is not iterable so we need to change it to...
# for x in 25:
# this next line prints
for x in [25]:

    print(x)

# Sample 4
# iterate Strings

# we create a function to call a List of String Arrays
def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)


# then we call our Function greet friends on a list of String Parameters
greet_friends(['Taylor', 'Luisa', 'Jamaal', 'Eli'])

# NOW if we use this next line, it will iterate EACH string
greet_friends("Barry")
