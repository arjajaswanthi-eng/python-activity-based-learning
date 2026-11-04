usage = [
    [2, 3, 2, 4, 3, 2, 3],
    [4, 4, 5, 4, 5, 4, 4],
    [3, 3, 4, 3, 4, 3, 3]
]

appliances = ["Fan", "AC", "Light"]

for i in range(3):
    print(appliances[i], "Total:", sum(usage[i]))

for j in range(7):
    daily = sum(usage[i][j] for i in range(3))
    print("Day", j + 1, ":", daily, "units")

    if daily > 15:
        print("High Consumption Alert")
