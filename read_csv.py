import csv

prices = []

with open("prices.csv") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        price = int(row[1])
        prices.append(price)

print(prices)