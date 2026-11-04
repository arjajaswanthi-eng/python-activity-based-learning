classrooms = [
    ["A", None, "R", None, "B"],
    [None, "C", None, "D", "R"]
]

students = ["Teja", "Ravi", "Priya"]

for student in students:
    allocated = False
    for room in classrooms:
        for i in range(len(room)):
            if room[i] is None:
                room[i] = student
                allocated = True
                break
        if allocated:
            break

print("Classroom Occupancy:")
for i, room in enumerate(classrooms):
    print("Classroom", i + 1, ":", room)

all_students = []
for room in classrooms:
    for seat in room:
        if seat is not None and seat != "R":
            all_students.append(seat)

duplicates = [s for s in set(all_students)
              if all_students.count(s) > 1]

vacant = sum(room.count(None) for room in classrooms)

print("Duplicate Students:", duplicates)
print("Vacant Seats:", vacant)
