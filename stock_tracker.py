stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140
}

total = 0

while True:
    name = input("Enter stock name (or 'done'): ")

    if name == "done":
        break

    qty = int(input("Enter quantity: "))

    if name in stocks:
        total += stocks[name] * qty
    else:
        print("Stock not found")

print("Total Investment:", total)