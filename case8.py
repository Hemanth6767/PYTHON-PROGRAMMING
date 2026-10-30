
products = [
    ("Laptop", 50000, 5),
    ("Mouse", 500, 10),
    ("Keyboard", 1000, 2)
]

for name, price, stock in products:
    print("Product:", name)
    print("Price:", price)
    print("Stock:", stock)
    print("Total value:", price * stock)

    if stock < 5:
        print("Reorder required")
    print()
