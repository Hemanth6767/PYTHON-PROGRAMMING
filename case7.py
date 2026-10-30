
usage = [
    [10, 12, 15, 10, 14, 13, 12],
    [5, 6, 7, 5, 6, 8, 7]
]

for i in range(len(usage)):
    total = sum(usage[i])
    print("Appliance", i + 1)
    print("Weekly consumption:", total, "units")
