teams = {
    "India": [0, 0],
    "Australia": [0, 0],
    "England": [0, 0]
}

matches = [
    ("India", "Australia", 3, 1),
    ("England", "India", 2, 2),
    ("Australia", "England", 4, 2)
]

for a, b, sa, sb in matches:
    teams[a][1] += sa - sb
    teams[b][1] += sb - sa

    if sa > sb:
        teams[a][0] += 3
    elif sb > sa:
        teams[b][0] += 3
    else:
        teams[a][0] += 1
        teams[b][0] += 1

ranking = sorted(
    teams.items(),
    key=lambda x: (x[1][0], x[1][1]),
    reverse=True
)

print("Tournament Rankings:")
for i, (name, values) in enumerate(ranking, 1):
    print(i, name, "Points:", values[0],
          "Difference:", values[1])
