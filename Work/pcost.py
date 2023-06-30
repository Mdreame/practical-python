# pcost.py
#
# Exercise 1.27
import csv

def portfolio_cost(file):
    try:
        with open(file, 'rt') as f:
            next(f)
            total = 0
            rows = csv.reader(f)
            
            for row in rows:
                total = total + int(row[1]) * float(row[2])

        return total
    # error name must match the error type
    except FileNotFoundError:
        print('no such file: %s' % file)

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost', cost)