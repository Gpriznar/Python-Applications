number = int(input('Please enter a number = '))

if number > 1:
    for index in range(2, number):
        if (number % index) == 0:
            print("Your number is not a prime number")
            break
    else:
        print("Your number is a prime number")
else:
    print(f"{number} is not a prime number")
