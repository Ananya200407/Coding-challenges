try:
    item_code = input("Enter item code: ").strip()
    description = input("Enter item description: ").strip()
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    if quantity < 0 or price < 0:
        print("Quantity and price must be non-negative values.")
    else:
        total_cost = quantity * price

        print("\n--- Item Bill Details ---")
        print("Item Code:", item_code)
        print("Description:", description)
        print("Quantity:", quantity)
        print("Price per Item: Rs.", price)
        print("Total Cost: Rs.", total_cost)

except ValueError:
    print("Invalid input! Please enter numeric values for quantity and price.")
