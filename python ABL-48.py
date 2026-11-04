shifts = [
    ("Ravi", 9, 13),
    ("Teja", 10, 14),
    ("Ravi", 12, 16),
    ("Priya", 14, 18)
]

found = False

for i in range(len(shifts)):
    for j in range(i + 1, len(shifts)):
        name1, start1, end1 = shifts[i]
        name2, start2, end2 = shifts[j]

        if name1 == name2:
            if start1 < end2 and start2 < end1:
                print("Conflict:", name1)
                print("Shift 1:", start1, "-", end1)
                print("Shift 2:", start2, "-", end2)
                found = True

if not found:
    print("No Conflicts Found")
