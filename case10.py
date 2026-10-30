
old_prices = [100, 200, 300]
new_prices = [120, 180, 330]

for i in range(3):
    change = ((new_prices[i] - old_prices[i])
              / old_prices[i]) * 100

    print("Product", i + 1)
    print("Price change:", change, "%")

    if change > 10:
        print("Price increased")
    elif change < 0:
        print("Price decreased")
    else:
        print("Normal change")
