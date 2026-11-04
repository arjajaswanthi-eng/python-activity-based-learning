inventory = [
    [25, 15, 30],
    [10, 25, 18]
]

products = ["Laptop", "Mouse", "Keyboard"]
target = 20

for i in range(2):
    print("Warehouse", i + 1)

    for j in range(3):
        difference = inventory[i][j] - target

        if difference < 0:
            print(products[j], "Shortage:", -difference)
        elif difference > 0:
            print(products[j], "Surplus:", difference)
        else:
            print(products[j], "Stock Balanced")
