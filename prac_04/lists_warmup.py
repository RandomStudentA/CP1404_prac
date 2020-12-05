numbers = [3, 1, 4, 1, 5, 9, 2]

# What I thought it would print: 3
# What it printed: 3
print(numbers[0])

# What I thought it would print: 2
# What it printed: 2
print(numbers[-1])

# What I thought it would print: 1
# What it printed: 1
print(numbers[3])

# What I thought it would print: 2
# What it printed: [3, 1, 4, 1, 5, 9]
print(numbers[:-1])

# What I thought it would print: 1, 5
# What it printed: 1
print(numbers[3:4])

# What I thought it would print: True
# What it printed: True
print(5 in numbers)

# What I thought it would print: False
# What it printed: False
print(7 in numbers)

# What I thought it would print: False
# What it printed: 0
print("3" in numbers)

# What I thought it would print: 3, 1, 4, 1, 5, 9, 2, 6, 5, 3
# What it printed: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(numbers + [6, 5, 3])

# Question 1
numbers[0] = "ten"
print(numbers)

# Question 2
numbers[-1] = 1
print(numbers)

# Question 3
print(numbers[2:7])

# Question 4
print(9 in numbers)
