no1 = int(input(f'Enter your first number = '))
sign = input(f'Enter your operator = ')
no2 = int(input(f'Enter your third number = '))

# addition

def add(no1,no2):
    sum = no1 + no2
    return sum

add_answer = add(no1,no2)

# subtraction

def subtract(no1,no2):
    difference = no1 - no2
    return difference

sub_answer = subtract(no1,no2)

# multiplication

def multiply(no,no2):
    value = no1 * no2
    return value

mult_answer = multiply(no1,no2)

# division

def divide(no1,no2):
    total = no1 / no2
    return total

div_answer = divide(no1,no2)

# Operator Conditions

if sign == "+":
    print(add_answer)
elif sign == "-":
    print(sub_answer)
elif sign == "*":
    print(mult_answer)
elif sign == "/":
    print(div_answer)
else:
    print("Invalid Operator")
