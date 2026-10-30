
prepared = [100, 120, 150]
served = [90, 100, 130]

for i in range(3):
    waste = prepared[i] - served[i]
    percentage = (waste / prepared[i]) * 100

    print("Day", i + 1)
    print("Food wasted:", waste)
    print("Waste percentage:", percentage, "%")
