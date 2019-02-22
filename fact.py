number = int(input('Please enter a number = '))
factorial = 1

for index in range(1,number +1):
         factorial = factorial * index

print(f"The factorial of {number} is {factorial}")
