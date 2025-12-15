try:
    grand_total = 0.0

    n = int(input("Enter number of items: "))

    if n <= 0:
        print("Number of items must be greater than 0.")
    else:
        for i in range(1, n + 1):
            print(f"\nEnter details for Item {i}")

            item_code = input("Item code: ").strip()
            description = input("Description: ").strip()
            quantity = int(input("Quantity: "))
            price = float(input("Price per item: "))

            if quantity < 0 or price < 0:
                print("Quantity and price must be non-negative. Item skipped.")
                continue

            item_total = quantity * price
            grand_total += item_total

            print("Item Total: Rs.", item_total)

        print("\n========================")
        print("Grand Total: Rs.", grand_total)
        print("========================")

except ValueError:
    print("Invalid input! Please enter numeric values correctly.")
