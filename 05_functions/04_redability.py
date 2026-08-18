def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

price = calculate_bill(3,15)
print(f"Total Bill: {price}")

print("Order for table 2: ",calculate_bill(2,50))

