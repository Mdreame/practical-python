# pcost.py
#
# Exercise 1.27
def portfolio_cost(file):
    with open(file, 'rt') as f:
        header = next(f)
        total = 0

        for line in f:
            row = line.split(',')
            total = total + int(row[1]) * float(row[2])

    return total
cost = portfolio_cost('Data/portfolio.csv')
print('Total cost', cost)