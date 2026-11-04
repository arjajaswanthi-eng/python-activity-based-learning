marks = [
    [85, 90, 78],
    [70, 65, 80],
    [95, 92, 96]
]

names = ["Teja", "Ravi", "Priya"]
subjects = ["Python", "Maths", "English"]

totals = []
for row in marks:
    totals.append(sum(row))

averages = [total / 3 for total in totals]

for i in range(3):
    print(names[i], "Total:", totals[i],
          "Average:", averages[i])

top = totals.index(max(totals))
print("Top Performer:", names[top])

for j in range(3):
    avg = sum(marks[i][j] for i in range(3)) / 3
    print(subjects[j], "Average:", avg)
    if avg < 40:
        print("Low Performing Subject:", subjects[j])
