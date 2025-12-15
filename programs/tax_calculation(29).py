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
        print("Subtotal: Rs.", grand_total)

        if grand_total > 10000:
            discount_10 = grand_total * 0.10
            grand_total -= discount_10
            print("10% Discount Applied: -Rs.", discount_10)

        if total_quantity > 20:
            discount_5 = grand_total * 0.05
            grand_total -= discount_5
            print("5% Quantity Discount Applied: -Rs.", discount_5)

        member = input("Is the customer a member? (y/n): ").strip().lower()
        if member == 'y':
            discount_2 = grand_total * 0.02
            grand_total -= discount_2
            print("2% Membership Discount Applied: -Rs.", discount_2)

        print("Amount After Discounts: Rs.", round(grand_total, 2))

        # TAX CALCULATION 
        if grand_total < 5000:
            tax_rate = 0.05
        elif grand_total <= 20000:
            tax_rate = 0.10
        else:
            tax_rate = 0.15

        tax_amount = grand_total * tax_rate
        final_total = grand_total + tax_amount

        print(f"Tax Applied ({int(tax_rate*100)}%): Rs.", round(tax_amount, 2))
        print("--------------------------")
        print("Final Payable Amount: Rs.", round(final_total, 2))
        print("--------------------------")

except ValueError:
    print("Invalid input! Please enter numeric values correctly.")
