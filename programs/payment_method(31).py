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

            if item_code == "PROMO10":
                discount = item_total * 0.10
                item_total -= discount
                print("Promotional Discount Applied (10%): -Rs.", discount)

            grand_total += item_total
            print("Item Total: Rs.", round(item_total, 2))

        print("\nSubtotal after discounts: Rs.", round(grand_total, 2))

        # -------- Payment Method --------
        payment_method = input("Select payment method (cash/card): ").strip().lower()

        surcharge = 0.0
        if payment_method == "card":
            surcharge = grand_total * 0.02
            grand_total += surcharge
            method = "Credit Card"
            print("2% Credit Card Surcharge Applied: +Rs.", round(surcharge, 2))
        elif payment_method == "cash":
            method = "Cash"
            print("No surcharge applied for Cash payment.")
        else:
            method = "Unknown"
            print("Invalid payment method selected. No surcharge applied.")

        print("\n------ PAYMENT SUMMARY ------")
        print("Payment Method:", method)
        print("Surcharge: Rs.", round(surcharge, 2))
        print("Final Payable Amount: Rs.", round(grand_total, 2))
        print("-----------------------------")

except ValueError:
    print("Invalid input! Please enter numeric values correctly.")
