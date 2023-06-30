# pcost.py
#
# Exercise 1.27
with open('Data/portfolio.csv', 'rt') as f:
    header = next(f)
    total = 0

    for line in f:
        row = line.split(',')
        total = total + int(row[1]) * float(row[2])

print('Total cost', total)