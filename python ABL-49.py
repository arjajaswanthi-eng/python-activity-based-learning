products = [
    ("P101", 500, 20),
    ("P102", 300, 5),
    ("P103", -100, 10),
    ("P104", 700, 0)
]

total_value = 0

for pid, price, stock in products:

    if price <= 0 or stock < 0:
        print(pid, "Invalid Record")
        continue

    value = price * stock
    total_value += value

    print(pid, "Inventory Value:", value)

    if stock < 10:
        print("Replenishment Required")

print("Total Inventory Value:", total_value)
