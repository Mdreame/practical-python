# mortgage.py
#
# Exercise 1.8
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 1

    #默认参数的使用
def set_extra_payment(start, end, extra, payment=2684.11):
    if start < months < end:
        payment = payment + extra

    return  payment


while principal > 0:
    payment = set_extra_payment(61, 108, 1000)

    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    # Python中的选择运算符, 此处为表达式
    result = f'{months:^3} \
        {total_paid:>9.2f} \
        {0 if principal < 0 else principal :0.2f}'

    print(result)

    months = months + 1

print(f'Total{total_paid:>16.2f}')

