# Question 1
output_file = "name.txt"

out_file = open(output_file, 'w')

name = str(input("Enter your name: "))

print(name, file=out_file)

out_file.close()

# Question 2
file = open('name.txt', 'r')
print("Your name is " + file.readline())

# Question 3
file = open('numbers.txt', 'r')
first_number = file.readline()
second_number = file.readline()

answer = int(first_number) + int(second_number)
print(answer)

# Question 4
file = open('numbers.txt', 'r')

count = 0
total = 0

# For loop to read total number of lines in it by adding +1 to count every line read and save to count
for line in open('numbers.txt').readlines():
    count += 1

# Loop the amount of times there is lines due to count
for i in range(count):
    number = file.readline()
    total += int(number)

print(total)
