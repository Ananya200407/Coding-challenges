try:
    grand_total = 0.0
    total_quantity = 0

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
            total_quantity += quantity

            print("Item Total: Rs.", item_total)

        print("\n------ BILL SUMMARY ------")
        print("Total Quantity:", total_quantity)
        print("Initial Grand Total: Rs.", grand_total)

        if grand_total > 10000:
            discount_10 = grand_total * 0.10
            grand_total -= discount_10
            print("10% Discount Applied: -Rs.", discount_10)
        else:
            print("No 10% Discount Applied")

        if total_quantity > 20:
            discount_5 = grand_total * 0.05
            grand_total -= discount_5
            print("Additional 5% Quantity Discount Applied: -Rs.", discount_5)
        else:
            print("No Quantity Discount Applied")

        print("--------------------------")
        print("Final Payable Amount: Rs.", round(grand_total, 2))
        print("--------------------------")

except ValueError:
    print("Invalid input! Please enter numeric values correctly.")
