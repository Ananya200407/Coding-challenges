try:
    grand_total = 0.0

    n = int(input("Enter number of items: "))

    if n <= 0:
        print("Number of items must be greater than 0.")
    else:
        for i in range(1, n + 1):
            print(f"\nEnter details for Item {i}")

            item_code = input("Item code: ").strip().upper()
            description = input("Description: ").strip()
            quantity = int(input("Quantity: "))
            price = float(input("Price per item: "))

            if quantity < 0 or price < 0:
                print("Quantity and price must be non-negative. Item skipped.")
                continue

            item_total = quantity * price

            # Promotional discount
            if item_code == "PROMO10":
                discount = item_total * 0.10
                item_total -= discount
                print("Promotional Discount Applied (10%): -Rs.", discount)
            else:
                print("No Promotional Discount Applied")

            grand_total += item_total

            print("Final Item Total: Rs.", round(item_total, 2))

        print("\n========================")
        print("Grand Total: Rs.", round(grand_total, 2))
        print("========================")

except ValueError:
    print("Invalid input! Please enter numeric values correctly.")
