# pcost.py
#
# Exercise 1.27
import csv
import sys


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

if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    file = 'Data/portfolio.csv' 

cost = portfolio_cost(file)

if cost:
    print('Total cost', cost)