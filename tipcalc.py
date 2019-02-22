total = float(input(f'Enter Total Amount = '))
tip = float(input(f'Enter Tip Percentage = '))

def divide(total,tip):
    tip = tip / 100
    return (total * tip)

tip_amount = divide(total, tip)
print(f'Your tip amount is ${tip_amount}')
