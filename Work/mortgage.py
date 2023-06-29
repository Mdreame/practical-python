# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
times = 0

while principal > 0:

    # 难点在于区分何时需要循环、合适需要判断
    # 此处不需要对前12个月建立倒数计时
    if times < 12:
        # payment = payment  + 1000
        # 这是不对的，每次更新都会改变全局变量payment
        payment = 3684.11
    else:
        payment = 2684.11

    print(payment, times)
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    
    times = times + 1

print('Total paid', total_paid)

