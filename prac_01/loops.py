# An alternative way to calculate the display the odd number between 1 to 20
for i in range(1, 21):
    if i % 2 != 0:
        print(i)

# Starting from 0 to 101, every 10 difference is shows
for i in range(0, 101, 10):
    print(i)

# Starting from 20 all the way to 0, every step -1
for i in range(20, 0, -1):
    print(i)

stars = int(input("Number of stars : "))
# Loop the amount of times that user entered for "stars", alternative of " for i in range(1, stars + 1, +1): "
for i in range(stars):
    # Print starts while " end="" " makes a space to be printed between each stars rather than in a new line
    print("*", end="")

# For self reference, print("*", "*" * i, end="") wil print * ** *** ***** *****

stars = int(input("Number of stars : "))
# 1 is the number is start with, + 1 on stars because loop starts with 0 and not 1, so + 1 is needed
for i in range(1, stars + 1):
    # i is the amount of times it looped, it was set as 1 so it starts at 1 instead of 0.
    print("*" * i)
