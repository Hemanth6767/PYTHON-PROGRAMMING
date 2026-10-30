
marks = [
    [80, 75, 90],
    [65, 70, 85],
    [90, 95, 88]
]

for i in range(len(marks)):
    total = sum(marks[i])
    avg = total / len(marks[i])
    print("Student", i + 1)
    print("Total:", total)
    print("Average:", avg)
