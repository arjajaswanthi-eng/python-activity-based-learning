occupancy = [
    [7, 8, 9],
    [5, 12, 8],
    [6, 7, 9]
]

wards = ["General", "ICU", "Emergency"]
capacity = [10, 10, 10]

for i in range(3):
    total = sum(occupancy[i])
    percentage = (total / (capacity[i] * 3)) * 100

    print(wards[i], "Total Beds:", total)
    print("Utilization:", round(percentage, 2), "%")

    if max(occupancy[i]) > capacity[i]:
        print("Capacity Violation Detected")

peak = max(max(row) for row in occupancy)
print("Peak Occupancy:", peak)
