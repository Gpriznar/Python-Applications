### User Input ###

a = int(input(f'Enter your first number = '))
sign = input(f'Enter your operator = ')
b = int(input(f'Enter your third number = '))

### Calculator ###

class Calculator:
    def __init__(self):
        pass

    def add(self,a,b):
        print(f"The answer is {a+b}")

    def sub(self,a,b):
        print(f"The answer is {a-b}")

    def mult(self,a,b):
        print(f"The answer is {a*b}")

    def div(self,a,b):
        print(f"The answer is {a/b}")

calculator = Calculator()
### Conditionals ###

if sign == "+":
    calculator.add(a,b)
elif sign == "-":
    calculator.sub(a,b,)
elif sign == "*":
    calculator.mult(a,b)
elif sign == "/":
    calculator.div(a,b)
else:
    print("Invalid Operator")
