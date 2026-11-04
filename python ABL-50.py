import math

routes = [
    (0, 0),
    (3, 4),
    (6, 8),
    (12, 8)
]

distances = []

for i in range(len(routes) - 1):
    x1, y1 = routes[i]
    x2, y2 = routes[i + 1]

    distance = math.sqrt(
        (x2 - x1)**2 + (y2 - y1)**2
    )

    distances.append(distance)

    print("Segment", i + 1, "Distance:",
          round(distance, 2), "km")

print("Total Distance:", round(sum(distances), 2), "km")

longest = max(distances)
index = distances.index(longest) + 1

print("Longest Segment:", index)
print("Longest Distance:", round(longest, 2), "km")
