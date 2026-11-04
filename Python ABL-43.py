sales = [
    [100, 150, 200],
    [250, 200, 180],
    [150, 300, 250]
]

products = ["Laptop", "Mobile", "Tablet"]
branches = ["Branch A", "Branch B", "Branch C"]

for i in range(3):
    print(products[i], "Total:", sum(sales[i]))

for j in range(3):
    total = sum(sales[i][j] for i in range(3))
    best = max(range(3), key=lambda i: sales[i][j])
    print(branches[j], "Sales:", total)
    print("Best Product:", products[best])
