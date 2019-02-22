number = int(input(f'Please enter a number = '))

def picker(number):
    value = number % 2
    return number

answer = picker(number%2)

if answer == 0:
    print (f"Your number is even")
elif answer == 1:
    print (f'Your number is odd')
